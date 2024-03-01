from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'nat_id', 'father_name', 'date_of_birth', 'phone_number', 'country', 'city'
                    , 'gender', 'job', 'vip', 'datetime_created', )

    ordering = ('datetime_created',)

