from django.urls import path
from currrent_location import views as current_view

urlpatterns = [
    path('current_location', current_view.get_current_location, name='get_current_location'),
    path('location', current_view.GetCurrentLocationaManualy.as_view(), name='location'),
    path('select_location/<int:pk>', current_view.select_country_city_view, name='select_location'),
]