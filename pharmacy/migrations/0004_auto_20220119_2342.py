# Generated by Django 3.2.8 on 2022-01-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_auto_20220119_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='end_time',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='start_time',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
