from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from myapp.models import Student

def signupPage(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")

        if pass1!=pass2:
            return HttpResponse("Password not match")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect("loginPage")

    return render(request,"signup.html")




def loginPage(request):
    
     if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(request,username=username,password=pass1)
        if user!=None:
            login(request,user)
            return redirect("homePage")
        else:
            return HttpResponse("username not found")
    
     return render(request,"login.html")


def homePage(request):
    user=request.user
    emp=Student.objects.all()
    return render(request, 'home.html', {'user_name': user, 'emp': emp})


# Add item

def addPage(request):
    myName=request.POST.get("name")
    myEmail=request.POST.get("email")
    mySemester=request.POST.get("semester")
    myAddress=request.POST.get("address")
    myPhone=request.POST.get("phone")
    myBatch=request.POST.get("batch")

    emp = Student(
        name=myName,
        email=myEmail,
        semester = mySemester,
        address=myAddress,
        phone=myPhone,
        batch=myBatch,
    )
    emp.save()
    return redirect('homePage')



# # Update or Edit page
# def updatePage(request,id):
#     if request.method=="POST":
#         myName=request.POST.get("name")
#         myEmail=request.POST.get("email")
#         myAddress=request.POST.get("address")
#         myPhone=request.POST.get("phone")
        
#         emp=Student(
#             id=id,
#             name=myName,
#             email=myEmail,
#             address=myAddress,
#             mobile=myPhone
            
#         )
        
#         emp.save()
#         return redirect("homePage")


# # Delete =======================

# def deletePage(request,id):
#     emp=Student.objects.filter(id=id)
#     emp.delete()
#     return redirect("homePage")