from django.urls import path
from currrent_location import views

urlpatterns = [
    path('current_location', views.get_current_location, name='get_current_location'),
    path('location', views.GetCurrentLocationaManualy.as_view(), name='location'),
    path('select_location/<int:pk>', views.select_country_city_view, name='select_location'),
]