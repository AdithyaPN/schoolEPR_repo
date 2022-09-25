from django.urls import path
from . import views

urlpatterns=[
    path('studenthome', views.student_home),
    path('profile', views.student_profile),
    path('changepassword', views.password_change),
]