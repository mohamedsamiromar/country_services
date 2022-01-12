# Generated by Django 3.2.8 on 2022-01-10 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResturantRegisterApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('user_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=155, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('start_working', models.DateTimeField(blank=True, null=True)),
                ('end_working', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[(201, 'Open'), (405, 'Closed')], default='Open', max_length=155)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResturantBookingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
                ('user_mobile_number', models.CharField(blank=True, max_length=11, null=True)),
                ('table_booking_number', models.IntegerField(blank=True, null=True)),
                ('chair_booking_number', models.IntegerField(blank=True, null=True)),
                ('booking_hourse', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResturanProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(blank=True, default=False, max_length=150, null=True)),
                ('address', models.CharField(blank=True, default=False, max_length=155, null=True)),
                ('email', models.EmailField(blank=True, default=False, max_length=254, null=True, unique=True)),
                ('city', models.CharField(blank=True, default=False, max_length=75, null=True)),
                ('country', models.CharField(blank=True, default=False, max_length=75, null=True)),
                ('occupied_table', models.IntegerField(blank=True, default=False, null=True)),
                ('available_table', models.IntegerField(blank=True, default=False, null=True)),
                ('menu', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DelivaryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
                ('order_count', models.IntegerField(blank=True, null=True)),
                ('user_mobile_number', models.CharField(blank=True, max_length=11, null=True)),
                ('resturant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.resturanprofile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]