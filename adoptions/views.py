from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def home(request):
    pet=Pet.objects.all()
    return render(request,'home.html',{'pets':pets})
    #return HttpResponse('<p>home view </p>')


def pet_detail(request,id):  
    try:  
        pet=Pet.object.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request,'pet_home.html',{'pet':pet})  
    #return HttpResponse('<p>deatl {}</p>'.format(id))