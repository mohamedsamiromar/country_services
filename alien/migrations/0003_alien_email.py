# Generated by Django 3.2.8 on 2022-02-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alien', '0002_alien_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='alien',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
