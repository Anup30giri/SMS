from django.contrib import admin
from students.models import Students
from students.models import Teachers


# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)