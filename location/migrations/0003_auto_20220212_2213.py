# Generated by Django 3.2.8 on 2022-02-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20220211_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentlocation',
            name='city',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='currentlocation',
            name='country',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
