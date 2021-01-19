from django.contrib import admin
from .models import Student
# Register your models here.



class Admin_StudentInfo(admin.ModelAdmin):
    list_display = ['name','varsity_id','phone','address','email']



admin.site.register(Student,Admin_StudentInfo)