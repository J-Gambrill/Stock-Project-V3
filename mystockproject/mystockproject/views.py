#This file just respons to request for the given page
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

