# Generated by Django 3.2.8 on 2022-05-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_auto_20220227_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='status',
        ),
    ]
