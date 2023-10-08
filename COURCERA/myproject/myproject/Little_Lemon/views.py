from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Bienvenido a Little Lemon! </h1>") 
# Create your views here.

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")

