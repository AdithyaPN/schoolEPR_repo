import imp
from django.shortcuts import render
import os

# Create your views here.
def teacher_home(request):
    return render(request, 'teachertemplates/home.html')