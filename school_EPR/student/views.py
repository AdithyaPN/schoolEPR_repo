import imp
from django.shortcuts import render
import os

# Create your views here.
def student_home(request):
    return render(request, 'studenttemplates/studenthome.html')

def student_profile(request):
    return render(request, 'studenttemplates/profile.html')

def password_change(request):
    return render(request, 'studenttemplates/changepassword.html')