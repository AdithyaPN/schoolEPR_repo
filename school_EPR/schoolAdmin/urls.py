from django.urls import path
from . import views

urlpatterns=[
    path('', views.admin_home),
    path('viewstaff', views.view_staff),
    path('addstaff', views.add_staff),
    path('viewstudent', views.view_student),
    path('login', views.login_page),
    path('timetable', views.time_table),
    path('contact', views.contact_us),
    path('about', views.about_us),
    path('scholarship', views.scholarship),
]
