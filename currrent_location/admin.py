from django.contrib import admin

# Register your models here.
from currrent_location.models import CurrentLocation, GetLocationManual, City

admin.site.register(CurrentLocation)
admin.site.register(GetLocationManual)
admin.site.register(City)
