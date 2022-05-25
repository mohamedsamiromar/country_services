from django.urls import path, include
from rest_framework.routers import DefaultRouter
from park import  views


urlpatterns = [
    path('api-profiles-park', views.ParkRegisterView.as_view(), name='api-profiles-park')
]