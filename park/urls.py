from django.urls import path, include
from rest_framework.routers import DefaultRouter
from park import  views

router = DefaultRouter()
router.register('api-profiles-park/', views.ParkRegisterView, basename='park')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]