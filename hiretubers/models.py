from django.db import models
from datetime import datetime
# Create your models here.
class Hiretuber(models.Model):
    first_name=models.CharField(max_length=100 ,default="first_name")
    last_name=models.CharField(max_length=100 ,default="last_name")
    tuber_id=models.IntegerField()
    tuber_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    phone=models.IntegerField(blank=True)
    email=models.EmailField()
    state=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    user_id=models.IntegerField( blank=True)
    
    created_date=models.DateTimeField(blank=True, default= datetime.now)

    
    


    def __str__(self):
       return self.email
