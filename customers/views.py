from django.shortcuts import render
from django.views import generic

from .models import Customer


class CustomersList(generic.ListView):
    template_name = "customers/customers_list.html"
    model = Customer
    context_object_name = 'customers_list'


