from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    varsity_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=200)
    email = models.CharField(max_length=40, unique=True)
