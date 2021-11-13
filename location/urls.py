from django.urls import path
from location import views

urlpatterns = [
    path('current_location', views.get_current_location, name='get_current_location')
]