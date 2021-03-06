# Generated by Django 3.2.8 on 2022-02-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20220212_2213'),
        ('alien', '0003_alien_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alien',
            name='residence',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='location.currentlocation'),
        ),
        migrations.DeleteModel(
            name='Residence',
        ),
    ]
