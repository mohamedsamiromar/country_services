# Generated by Django 3.2.8 on 2022-02-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_auto_20220219_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='country',
            field=models.CharField(blank=True, choices=[('FRA', 'French'), ('SWZ', 'Switzerland'), ('BLG', 'Belgium')], default=False, max_length=55, null=True),
        ),
    ]
