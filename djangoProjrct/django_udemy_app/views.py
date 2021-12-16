from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student

def index(request):
    if request.method=='GET':
        return render(request,"index.html")

    if request.method=='POST':
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        if gender=='male':
            gender="male"
        elif gender=='female':
            gender="female"
        else:
            gender="other"
        mobile_no=request.POST.get('mobile')
        stud=Student(
            firstname=fname,
            middlename=mname,
            lastname=lname,
            gender=gender,
            mobile_no=mobile_no
        )
        stud.save()
        return render(request,'index.html',{'message':"Save Successfully"})
# Create your views here.
