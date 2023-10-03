from django.db import models
from django.conf import settings

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    semester=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.IntegerField()
    batch=models.CharField(max_length=200)

class img(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image=models.ImageField(upload_to='img', null=True, blank=True)
   
#         return self.name

# class img(models.Model):
#     name=models.CharField(max_length=20)
#     des=models.TextField()
#     image=models.ImageField(upload_to='img', null=True, blank=True)
#     def __str__(self):
#         return self.name