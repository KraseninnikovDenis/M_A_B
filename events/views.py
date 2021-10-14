from django.shortcuts import render
from .models import EventsDB

def home(request):
    events=EventsDB.objects
    return render(request,'events/home.html', {'events':events})
