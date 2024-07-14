from django.shortcuts import render, redirect
from .models import Complaint

# Create your views here.


def add_complaint(req):
    if req.method == 'POST':
        complaint = Complaint.objects.create(
            user=req.user,
            category=req.POST.get('complaint_type'),
            body=req.POST.get('complaint_text')
        )
        return redirect('base:home')

    return render(req, 'complaints/complaint.html')


def update_complaint(req):
    if req.method == 'POST':
        for id in req.POST.keys():
            try:
                complaint = Complaint.objects.get(id=id)
                complaint.status = True
                complaint.save()
            except:
                pass
        return redirect('base:home')
