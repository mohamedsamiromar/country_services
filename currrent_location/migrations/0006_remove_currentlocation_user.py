# Generated by Django 3.2.8 on 2021-11-19 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currrent_location', '0005_selectecountryandcity_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentlocation',
            name='user',
        ),
    ]