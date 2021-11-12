from django.urls import path
from . import  views

urlpatterns = [
    path('current_location', views.get_current_location, name='get_current_location')
]