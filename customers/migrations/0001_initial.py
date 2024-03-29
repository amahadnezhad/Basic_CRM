# Generated by Django 5.0.2 on 2024-02-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('nat_id', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=12)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=1)),
                ('job', models.CharField(max_length=100)),
                ('vip', models.BooleanField(default=False)),
                ('education', models.CharField(max_length=100)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
