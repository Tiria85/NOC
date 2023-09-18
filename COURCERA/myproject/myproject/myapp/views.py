from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> Bienvenido a Little Lemon! </h1>") 

def index(request):
    return HttpResponse("Hola mundo")