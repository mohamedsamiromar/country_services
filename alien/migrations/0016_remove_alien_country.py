# Generated by Django 3.2.8 on 2022-05-05 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alien', '0015_auto_20220504_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alien',
            name='country',
        ),
    ]
