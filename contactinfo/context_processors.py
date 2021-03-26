
#return value of this avail for all templates


from .models import Contactinfo

def contactinfo(request):
    contact=Contactinfo.objects.order_by('-created_date')
    data={"contactinfo" : contact[0]}
    return data