from django.shortcuts import render,HttpResponse

# Create your views here.
def students(request):
    return HttpResponse("this is students")