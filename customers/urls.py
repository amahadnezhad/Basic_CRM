from django.urls import path

from .views import CustomersList, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
    path('', CustomersList.as_view(), name="customers_list"),
    path('add/', CustomerCreateView.as_view(), name="customer_create"),
    path('<int:pk>/update', CustomerUpdateView.as_view(), name="customer_update"),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name="customer_delete"),
]
