from django.urls import path

from .views import CustomersList, CustomerCreateView

urlpatterns = [
    path('', CustomersList.as_view(), name="customers_list"),
    path('add/', CustomerCreateView.as_view(), name="customer_create"),

]
