from django.contrib import admin
from myapp.models import Student,profileImg
from . import models

# Register your models here.
admin.site.register(Student)
admin.site.register(profileImg)
