from django.urls import path, include
from alien import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('alien_register', views.RegisterAlienView, basename='alien_register'),

urlpatterns = [
    path('', include(router.urls)),
]
