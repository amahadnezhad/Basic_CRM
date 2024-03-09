from django.urls import reverse_lazy
from django.views import generic

from .models import Customer
from .forms import CustomerForm


class CustomersList(generic.ListView):
    template_name = "customers/customers_list.html"
    model = Customer
    context_object_name = 'customers_list'


class CustomerCreateView(generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_create.html'
    success_url = reverse_lazy('customers_list')


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_url = reverse_lazy('customers_list')


class CustomerDeleteView(generic.DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    success_url = reverse_lazy('customers_list')
