# Generated by Django 3.2.8 on 2022-01-11 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_currentlocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentlocation',
            name='user',
        ),
    ]
