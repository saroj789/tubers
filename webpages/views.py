from django.shortcuts import render
from .models import Slider,Team,About
from youtubers.models import Youtubers
from contactinfo.models import Contactinfo

# Create your views here



def home(request):
    sliders = Slider.objects.all()
    data={'sliders': sliders}

    teams=Team.objects.all()
    data['teams']=teams

    featured_youtubers = Youtubers.objects.order_by('-created_date').filter(is_featured=True)
    data['featured_youtubers']=featured_youtubers

    all_tubers=Youtubers.objects.order_by('-created_date')
    data['all_tubers']=all_tubers   
   
    return render(request, "webpages/home.html",data)


def about(request):

    teams=Team.objects.all()
    data={'teams':teams}
    
    abouts=About.objects.order_by('created_date')
    data['abouts']= abouts
    
    return render(request, "webpages/about.html",data)

def services(request): 
    return render(request, "webpages/services.html")


def contact(request):
    
    return render(request, "webpages/contact.html")