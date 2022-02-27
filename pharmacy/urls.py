from django.urls import path, include
from pharmacy import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register-pharmacy', views.PharmacyView, basename='api-pharmacy'),

urlpatterns = [
    path('', include(router.urls)),
]
