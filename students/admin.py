from django.contrib import admin
from students.models import Students
from students.models import Teachers
from students.models import Employee


# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Employee)