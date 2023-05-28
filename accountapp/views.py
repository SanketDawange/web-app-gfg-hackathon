from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum, Max
from django.utils import timezone

from .models import Category, Hospital, Appointment, CustomUser

@csrf_exempt
def user_login(request):

    if request.method=="POST":
        username =request.POST.get('username')
        pass1  =request.POST.get('pass1')

        user=authenticate(username=username,password=pass1)

        if user is not None:
            if user.role != 'doctor':
                login(request,user)
                messages.info(request, "Logged in")
                return render(request,"home.html")
        else:
            messages.warning(request, "Invalid Credintials")
            return redirect('user_login')
    return render(request, "user/login.html")

@csrf_exempt
def user_signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1  = request.POST.get('pass1')
        pass2  = request.POST.get('pass2')

        if pass1 != pass2:
            messages.warning(request, "Password do not match")
            return redirect('user_signup')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, "Username already exist")
            return redirect('user_signup')
        
        myuser=CustomUser.objects.create_user(username,email,pass1)
        myuser.role = 'patient'
        myuser.save()

        messages.success(request, "Your account has been created successfully!")
        return redirect('user_login')

    return render(request, "user/signup.html")

def user_logout(request):

    if request.user.is_authenticated == False:
        return redirect("user_login")
    logout(request)
    return redirect("user_login")



def home(request):
    if request.user.is_authenticated == False:
        return redirect("user_login")
    
    return render(request, "home.html")

def schedule(request):

    if request.user.is_authenticated == False:
        return redirect("user_login")
    if request.method == "POST":
        category = request.POST.get('category')
        hospital = request.POST.get('hospital')
        reason = request.POST.get('reason')
        user = request.user

        newAppointment = Appointment(user=user, hospital=Hospital.objects.get(pk=hospital), category=Category.objects.get(pk=category), reason=reason)
        newAppointment.save()

        messages.info(request, "Appointment booked successfully! You will be notified soon")


    context = {"categories": Category.objects.all(), "hospitals": Hospital.objects.all()}
    return render(request, "schedule.html", context)