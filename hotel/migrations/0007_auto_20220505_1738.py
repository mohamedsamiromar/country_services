# Generated by Django 3.2.8 on 2022-05-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_hotel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='status',
        ),
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country',
            field=models.CharField(blank=True, choices=[('FRA', 'French'), ('SWZ', 'Switzerland'), ('BLG', 'Belgium')], default=False, max_length=55, null=True),
        ),
    ]
