from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Honey(request):
    return HttpResponse('<h1>Honey is cut girl</h1>')

def subbu(request):
    return HttpResponse('subbu is my friend')