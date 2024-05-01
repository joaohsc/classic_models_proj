from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def index(request):
    customers_count = Customers.objects.all().count()
    employees_count = Employees.objects.all().count()
    products_count = Products.objects.all().count()
    orders_count = Orders.objects.all().count()

    print(customers_count)

    context ={
        'customers_count': customers_count,
        'employees_count': employees_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'index.html', context)

def customers(request):
    customers = Customers.objects.all().order_by('customernumber')

    paginator = Paginator(customers, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)

def employees(request):
    employees = Employees.objects.all().order_by('employeenumber')

    paginator = Paginator(employees, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj': page_obj,
    }
    return render(request, 'employees.html', context)

def products(request):
    products = Products.objects.all().order_by('productcode')

    paginator = Paginator(products, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj': page_obj,
    }
    return render(request, 'products.html', context)