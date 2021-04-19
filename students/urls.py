from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students_list',views.get_student,name='students_list'),
    path('login',views.loginUser, name="login" ),
    path('logout',views.logoutUser,name="logout" ),
    path('registration',views.students,name="registration"),
    path('employee_reg',views.employee,name="employee_reg"),
    path('add_teacher',views.teachers,name="add_teacher"),
    path('update_student/<int:id>',views.update_student,name="update_student"), 
    path('employee_list',views.get_employee,name="employee_list"),
]
