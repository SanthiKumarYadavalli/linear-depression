from django.shortcuts import render, redirect
from complaints.models import Complaint

# Create your views here.


def home(req):
    if req.user.is_authenticated:
        if req.user.role:
            complaints = req.user.complaint_set.all()
        else:
            complaints = Complaint.objects.filter(
                user__block=req.user.username).filter(status=False)

        context = {'complaints': complaints}
        return render(req, 'base/home.html', context)
    return redirect('users:login-page')
