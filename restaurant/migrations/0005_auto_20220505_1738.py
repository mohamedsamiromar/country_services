# Generated by Django 3.2.8 on 2022-05-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurantprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='restaurantprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='restaurantprofile',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='restaurantprofile',
            name='status',
        ),
        migrations.AlterField(
            model_name='restaurantprofile',
            name='city',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantprofile',
            name='country',
            field=models.CharField(blank=True, choices=[('FRA', 'French'), ('SWZ', 'Switzerland'), ('BLG', 'Belgium')], default=False, max_length=55, null=True),
        ),
    ]