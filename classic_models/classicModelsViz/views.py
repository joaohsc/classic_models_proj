from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    customers = Customers.objects.all()
    
    context ={
        'customers':customers,
    }
    return render(request, 'index.html', context)