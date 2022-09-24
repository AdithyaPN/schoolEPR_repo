import imp
from django.shortcuts import render
import os

# Create your views here.
def teacher_home(request):
    return render(request, 'teachertemplates/home.html')

def add_student(request):
    return render(request, 'teachertemplates/addstudent.html')

def view_student(request):
    return render(request, 'teachertemplates/viewstudent.html')

def change_password(request):
    return render(request, 'teachertemplates/changepassword.html')