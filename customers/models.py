from django.db import models


class Customer(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nat_id = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=12)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    job = models.CharField(max_length=100)
    vip = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


