from django.urls import path
from currrent_location import views

urlpatterns = [
    path('current_location', views.get_current_location, name='get_current_location'),
    path('location', views.get_current_location_manual, name='location'),
    path('select_location', views.select_country_city, name='select_location'),
]