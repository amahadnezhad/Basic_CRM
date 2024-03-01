from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'nat_id', 'father_name', 'date_of_birth', 'phone_number', 'country', 'city',
                  'gender', 'job', 'vip', ]

