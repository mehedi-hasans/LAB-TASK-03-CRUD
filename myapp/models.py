from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    semester=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.IntegerField()
    batch=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class profileImg(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    image=models.ImageField(upload_to='img', null=True, blank=True)
    
   
#         return self.name

# class img(models.Model):
#     name=models.CharField(max_length=20)
#     des=models.TextField()
#     image=models.ImageField(upload_to='img', null=True, blank=True)
#     def __str__(self):
#         return self.name