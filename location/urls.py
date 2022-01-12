from django.urls import path
from location import views
from django_restful_admin import admin as api_admin

urlpatterns = [
    path('current_location', views.get_current_location, name='get_current_location'),
]