import imp
from django.shortcuts import render
import os

# Create your views here.
def admin_home(request):
    return render(request, 'schoolAdmintemplates/home.html')