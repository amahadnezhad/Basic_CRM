from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
        (3, _('Other')),
    )

    firstname = models.CharField(verbose_name=_("FirstName"), max_length=100)
    lastname = models.CharField(verbose_name=_("LastName"), max_length=100)
    nat_id = models.CharField(verbose_name=_("National_ID"), max_length=10)
    father_name = models.CharField(verbose_name=_("FatherName"), max_length=100)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"))
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=12)
    country = models.CharField(verbose_name=_("Country"), max_length=50)
    city = models.CharField(verbose_name=_("City"), max_length=50)
    gender = models.CharField(verbose_name=_("Gender"), choices=GENDER_CHOICES, max_length=1)
    job = models.CharField(verbose_name=_("Job"), max_length=100)
    vip = models.BooleanField(verbose_name=_("VIP"), default=False)

    datetime_created = models.DateTimeField(verbose_name=_("Created DateTime"), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_("Modified DateTime"), auto_now=True)

    def get_absolute_url(self):
        return reverse('customers_list', args=[self.id])
