from django.contrib import admin

# Register your models here.
from location.models import CurrentLocation

admin.site.register(CurrentLocation)

