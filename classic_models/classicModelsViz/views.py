from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def index(request):
    customers = Customers.objects.all()
    paginator = Paginator(customers, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)