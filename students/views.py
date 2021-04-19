from django.contrib.admin.decorators import register
from students.models import Employee, Students, Teachers
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from datetime import date, datetime



# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request,'index.html')


# ------Login---------------
def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # check if user have correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request,user)
            return redirect("/")
            # A backend authenticated credentials
        else:
            # No backedn authenticated the credentials
              return render(request,'login.html')
        

    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


#----------------- Students------
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
def get_student(request):
    students= Students.objects.all()
    
    return render(request,'students_list.html',{'students':students})


#  ---------------Update 
def update_student(request,id):
    students = Students.objects.get(id=id)
    if request.method == "POST":
        students.status = request.POST('status')
        students.name = request.POST('name')
        students.email = request.POST('email')
        students.gender = request.POST('gender')
        students.phone = request.POST('phone')
        students.address = request.POST('address')
        students.date = request.POST('date')
        students.desc = request.POST('desc')
        students.save()
        return redirect('studentslist.html')
    context={
        'students':students
        }
    return render(request,'update_student.html',context)


# -----------Teachers-------------
def teachers(request):

     if request.method == "POST":
        status = request.POST.get('status')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        # registration = (status= status,name = name,email=email,gender=gender,phone=phone,address=address,
        # desc=desc, date=date)
        # registration.save()
        messages.success(request, 'Teacher Has Been Added')
     return render(request,'add_teacher.html')

# -----------Employee------------
def employee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date = request.POST.get('date')
        employee = Employee(
        name = name,email=email,gender=gender,phone=phone,address=address, date=date)
        employee.save()
        messages.success(request, 'Employee Has Been Added')
    return render(request,"employee_reg.html")


    # -----------Display Employee-----
def get_employee(request):
    employee= Employee.objects.all()
    
    return render(request,'employee_list.html',{'employee':employee})


    # -----Update Employee----------------






  



    

