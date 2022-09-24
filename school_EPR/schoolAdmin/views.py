import imp
from django.shortcuts import render
import os

# Create your views here.
def admin_home(request):
    return render(request, 'schoolAdmintemplates/home.html')

def view_staff(request):
    return render(request, 'schoolAdmintemplates/viewStaff.html')

def add_staff(request):
    return render(request, 'schoolAdmintemplates/addStaff.html')

def view_student(request):
    return render(request, 'schoolAdmintemplates/viewstudent.html')