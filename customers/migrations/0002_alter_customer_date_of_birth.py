# Generated by Django 5.0.2 on 2024-02-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
