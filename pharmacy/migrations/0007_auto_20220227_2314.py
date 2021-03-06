# Generated by Django 3.2.8 on 2022-02-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0006_alter_pharmacy_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacy',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='location',
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='region_name',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='first_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='last_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='password',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
