from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.registerPage,name="login"),
    path('login',views.loginUser, name="login" ),
    path('logout',views.logoutUser,name="logout" ),

    path('user',views.userPage,name="user-page"),
    path('',views.index,name='index'),

    path('students_list',views.get_student,name='students_list'),
    path('registration',views.students,name="registration"),
    path('update_student/<int:id>',views.update_student,name="update_student"), 
    path('deleteStudent/<int:id>',views.deleteStudent),


    path('add_teacher',views.AddTeacherView.as_view(),name="add_teacher"),
    path('teachers', views.DisplayTeacherView.as_view(), name="display_teachers"),
    path('teachers/<int:pk>/update', views.UpdateTeacherView.as_view(), name="update_teachers"),
    path('teachers/<int:pk>/delete', views.DeleteTeacherView.as_view(), name="delete_teachers"),

    path('add_employee',views.AddEmployeeView.as_view(),name="add_employee"),
    path('display_employee',views.DisplayEmployeeView.as_view(),name="display_employee"),
    path('employee/<int:pk>/update', views.UpdateEmployeeView.as_view(), name="update_employee"),
    path('employee/<int:pk>/delete', views.DeleteEmployeeView.as_view(), name="delete_employee"),

]
