# Generated by Django 3.2.8 on 2022-04-11 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20220411_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantbooking',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_bookign', to='restaurant.restaurantprofile'),
        ),
    ]
