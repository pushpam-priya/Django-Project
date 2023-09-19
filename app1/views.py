import email
import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Dress
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User 
from django.contrib import messages 

# Create your views here.
# dresses=[
#     {'id':1,'type':'partywear'},
#     {'id':2,'type':'no-partywear'},
#     {'id':3,'type':'ok-partywear'},
#     {'id':4,'type':'nokay-partywear'}
# ]

def name(request):
    return render(request,'index.html',)
def about(request):
    messages.success(request,"Welcome to about")
    return render(request,'app1/about.html',)
def contact(request):
    messages.success(request,"Welcome to Contact")
    return render(request,'app1/contact.html',)


def handlelogin(request):
    messages.success(request,'Welcome to Loginpage')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
          login(request,user)
          print(username)
          return redirect(home)
        else:
          return HttpResponse("404-error")
    else:
        return HttpResponse("404-error")

def flogout(request):
    messages.success(request,"Logged out Successfully")
    logout(request)
    return render(request,'app1/login.html')
def loginpage(request):
    return render(request,'app1/login.html')



def home(request):
    if request.user.is_anonymous:
        return render(request,'app1/login.html')
    else:
        dresses= Dress.objects.all()
        params={'dresses':dresses}
        return render(request,'app1/home.html')



def signuppage(request):
    return render(request,'app1/signuppage.html')


def handleSignup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if(pass1 != pass2):
            return HttpResponse("<h1>password did not match!!!!!!!</h1>")

        usernew = User.objects.create_user(username=username, password=pass1)
        usernew.first_name=fname
        usernew.email=email
        usernew.last_name=lname
        usernew.save()
        messages.success(request," Account created successfully!")

        return render(request,"app1/login.html")
    else:
        return HttpResponse("404-Not Found")

    
def usereq(request):
    typehere=request.POST.get('type')
    genderhere=request.POST.get("gender")
    print(genderhere)
    if(genderhere=='1'):
        genderhere1="male"
    elif(genderhere=='2'):
        genderhere1="female"
    else:
        genderhere1=0
    print(genderhere1)
    queryset=Dress.objects.all()
    contents=queryset.filter(gender=str(genderhere1),type=str(typehere))
    context={'contents':contents}
    return render(request,"app1/result.html",context)
    

def result(request):
    return render(request,'app1/result.html')
