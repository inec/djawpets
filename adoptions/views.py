from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view </p>')


def pet_detail(request,id):    
    return HttpResponse('<p>deatl {}</p>'.format(id))