from django.urls import path
from . import views

urlpatterns=[
    path('home', views.teacher_home),
    path('addstudent', views.add_student),
    path('viewstudent', views.view_student),
    path('changepassword', views.change_password),
]