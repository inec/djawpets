from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view </p>')


def pet_details(request,id):    
    return HttpResponse('<p>deatl {}</p>'.format(id))