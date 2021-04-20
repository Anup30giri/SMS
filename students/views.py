from django.contrib.admin.decorators import register
from django.http.response import HttpResponse
from students.models import Students, Teachers,Employee
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from datetime import date, datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from.decorators import allowed_users, unathenticated_user,admin_only
from django.contrib.auth.models import Group
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy


# Create your views here.
@login_required(login_url="login")
def index(request):
    if request.user.is_anonymous:
        return redirect("/register")

    return render(request,'index.html')

# ------Admin---------------------
# --------Register Page------------
@unathenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,'Account Created for'+username)
            return redirect('login')


    context = {'form':form}
    return render(request,'accounts/register.html',context)

# ------Login Page----------------
@unathenticated_user
def loginUser(request):
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            # check if user have correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/register")
                # A backend authenticated credentials
            else:
                messages.info(request,'Username Or Password')
                # No backedn authenticated the credentials
                
        context={}

        return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect("/register")


# -----End Admin-----------

# -------User---------------
def userPage(request):
    return render(request,'accounts/user.html')


#----------------- Students------
@login_required(login_url="login")
@admin_only
def students(request):
    
      if request.method == "POST":
        status = request.POST.get('status')
        name = request.POST.get('name')
        email = request.POST.get('email')
        id = request.POST.get('id')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        students = Students(status= status,
        name = name,email=email,id=id,gender=gender,phone=phone,address=address,desc=desc, date=date)
        students.save()
        messages.success(request, 'Student Has Been Added')
      return render(request,"registration.html")


# -----------------Display Students-------------
@login_required(login_url="login")
def get_student(request):
    students= Students.objects.all()
    
    return render(request,'students_list.html',{'students':students})


#  ---------------Update 
@login_required(login_url="login")
@admin_only
def update_student(request,id):
    students = Students.objects.get(id=id)
    if request.method == "POST":
        students.status = request.POST['status']
        students.name = request.POST['name']
        students.email = request.POST['email']
        students.gender = request.POST['gender']
        students.phone = request.POST['phone']
        students.address = request.POST['address']
        # students.date = request.POST['date']
        students.save()
        messages.success(request, 'Student Has Been Updated')

        return redirect('students_list')
    context={
        'students':students
        }
    return render(request,'update_student.html',context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
# ---------Delete Students
def deleteStudent(request,id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect('students_list')



    # -----Update Employee----------------



class AddTeacherView(CreateView):
    model = Teachers
    fields = '__all__'
    template_name = 'add_teacher.html'
    success_url = reverse_lazy('display_teachers')


class DisplayTeacherView(ListView):
    model = Teachers
    template_name = 'display_teacher.html'


class UpdateTeacherView(UpdateView):
    model = Teachers
    fields = '__all__'
    template_name = 'update_teacher.html'
    success_url = reverse_lazy('display_teachers')
  

class DeleteTeacherView(DeleteView):
    model = Teachers
    template_name = 'delete_teachers.html'
    success_url = reverse_lazy('display_teachers')


class AddEmployeeView(CreateView):
    model = Employee
    fields='__all__'
    template_name='add_employee.html'
    success_url=reverse_lazy('display_employee')


class DisplayEmployeeView(ListView):
    model = Employee
    template_name = 'display_employee.html'

class UpdateEmployeeView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'update_employee.html'
    success_url = reverse_lazy('display_employee')

class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    success_url = reverse_lazy('display_employee')
