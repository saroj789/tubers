from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from hiretubers.models import Hiretuber

# Create your views here.

def login(request):
     
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(request,username=username,password=password)   # this object is available for all django templates by defaults
                                                                                # we can use User object  to chechk user is logged in or not
        if user is not None:
            auth.login(request,user)
            #print(user.is_authenticated)
            #print('login',request.user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')          

        else:
            messages.warning(request,'invalid crediantions')
            return redirect('login')

    return render(request,'accounts/login.html')



# we cannot create a func name as logout # becaause django has inbuilt logout fun
def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']


        if password==confirm_password and password!='':
            if  User.objects.filter(username=user_name).exists():
                messages.warning(request,'username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists() :
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password)
                    user.save()
                    messages.success(request,"Account created successfuly")
                    return redirect('login')

        else:
            messages.warning(request,'password do not match')
            return redirect('register')


    return render(request,'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    #print('dasgboard',request.user)

    #to show dashboard info from db
    hiretubers=Hiretuber.objects.filter(email=request.user.email)       # request.user is logged in user. if not logged in then it- AnnonymousUser
    data={ 'hiretubers' : hiretubers }  
    print(hiretubers)                                  
    return render(request,'accounts/dashboard.html',data)
