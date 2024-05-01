from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers", views.customers, name="customers"),
    path("employees", views.employees, name="employees"),
    path("products", views.products, name="products"),
]