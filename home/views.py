from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    context = {
        "variable1":"this is Ayush",
        "variable2":"this is Romy"
    }
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html', context)
def about(request):
     return render(request,'about.html')
def services(request):
    return render(request,'services.html')

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("/about")

        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request,'contact.html')
