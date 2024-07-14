from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_page(req):
    if req.user.is_authenticated:
        return redirect('base:home')
    return render(req, 'users/login.html')

def signup_student(req):
    if req.method == 'POST':
        user = User.objects.create_user(
            password=req.POST.get('student_password'),
            username=req.POST.get('student_id')
        )
        user.first_name = req.POST.get('student_name')
        user.block = req.POST.get('hostel_block')
        user.room = req.POST.get('room_number')
        user.email = req.POST.get('email')
        user.role = User.STUDENT
        user.save()
        login(req, user)
        return redirect('base:home')
    return render(req, 'users/login.html')


def signin_student(req):
    if req.method == 'POST':
        user = authenticate(req, username=req.POST.get('student_id'), password=req.POST.get('student_password'))
        if user is None:
            return redirect('users:login-page')
        login(req, user)
        return redirect('base:home')
    


def signup_admin(req):
    if req.method == 'POST':
        
        user = User.objects.create_user(
            password=req.POST.get('admin_password'),
            username=req.POST.get('admin_hostel')
        )
        user.first_name = req.POST.get('admin_name')
        user.email = req.POST.get('admin_email')
        user.role = User.WARDEN
        user.save()
        login(req, user)
        return redirect('base:home')
    return render(req, 'users/login.html')


def signin_admin(req):
    if req.method == 'POST':
        user = authenticate(req, username=req.POST.get('admin_hostel'), password=req.POST.get('admin_password'))
        if user is None:
            return redirect('users:login-page')
        login(req, user)
        return redirect('base:home')

def logout_page(req):
    logout(req)
    return render(req, 'users/login.html')
