from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

def login_page(request):
    # return HttpResponse("Hello World")
    if request.method == 'POST':
        email = request.POST['email'].strip()
        pwd = request.POST['password'].strip()
        try:
            chk_user = User.objects.get(email=email)
            user = authenticate(request, username=chk_user.username , password=pwd)
            if user is not None:
                login(request,user)
                return render(request, 'main_app/dashboard.html')
            else:
                messages.info(request,'Incorrect Email or Password !!!')
                return redirect('login_page')
        except:
            pass
    return render(request, 'main_app/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')



def register(request):
    # return HttpResponse("Hello World")
    if request.method == 'POST':
        email = request.POST['email'].strip()
        pwd = request.POST['password'].strip()
        c_pwd = request.POST['c_password'].strip()
        try:
            u=User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        if pwd != c_pwd:
            print("Password not Matched")
        else:
            c = User.objects.create_user(email,email,pwd,)
            messages.success(request,'User Registered Successfully !!!')
            return redirect('login_page')   
    return render(request, 'main_app/register.html')
