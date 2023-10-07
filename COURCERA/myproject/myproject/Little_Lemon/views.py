from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Bienvenido a Little Lemon! </h1>") 
# Create your views here.
