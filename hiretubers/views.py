from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages

# Create your views here.

    # first_name=models.CharField(max_length=100),
    # last_name=models.CharField(max_length=100),
    # tuber_id=models.IntegerField(max_length=100)
    # tuber_name=models.CharField(max_length=100)
    # city=models.CharField(max_length=100)
    # phone=models.IntegerField(max_length=100)
    # email=models.EmailField()
    # state=models.CharField(max_length=100)
    # message=models.TextField(max_length=100,blank=True)
    # user_id=models.IntegerField(max_length=100, blank=True)
    
   
def hiretuber(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        tuber_id=request.POST['tuber_id']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']
      
        print("first_name",first_name,"last_name", last_name,"tuber_id", tuber_id,"tuber_name" ,tuber_name,"city" ,city ,"phone", phone,"email", email,"state", state,"message", message,"user_id", user_id)
        # TODO: du all sanatization ( chacking msgs phone email etc validations )

        #hiretuber=Hiretuber()
        hiretuber=Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, city=city, phone=phone, email=email, state=state , message=message , user_id=user_id )
       
        print(hiretuber.first_name)
        hiretuber.save()
        messages.success(request,'Thanks for reching out!')
        return redirect('youtubers')
    else:
        return redirect('youtubers')
    
       
      
