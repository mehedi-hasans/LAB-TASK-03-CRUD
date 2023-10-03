from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    semester=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.IntegerField()
    batch=models.CharField(max_length=200)