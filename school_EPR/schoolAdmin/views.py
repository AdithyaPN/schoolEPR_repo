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

def login_page(request):
    return render(request, 'schoolAdmintemplates/login.html')

def time_table(request):
    return render(request, 'schoolAdmintemplates/timeTable.html')

def contact_us(request):
    return render(request, 'schoolAdmintemplates/contact.html')

def about_us(request):
    return render(request, 'schoolAdmintemplates/about.html')

def scholarship(request):
    return render(request, 'schoolAdmintemplates/scholarship.html')