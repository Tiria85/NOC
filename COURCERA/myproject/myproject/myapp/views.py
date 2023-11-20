from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Booking
from .forms import BookingForm

# Create your views here.

def home(request):
    return HttpResponse("<h1> Bienvenido a Little Lemon! </h1>") 

def index(request):
    return HttpResponse("Hola mundo")

def form_view(request):
     form = BookingForm()
     if request.method == 'POST':
         form = BookingForm(request.POST)
         if form.is_valid():
            form.save()
     context = {"form" : form}
     return render(request, "booking.html", context)