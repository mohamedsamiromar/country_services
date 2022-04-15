from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating import views

router = DefaultRouter()
router.register('restaurant-rating', views.RestaurantRateView, basename='restaurant-rating'),

urlpatterns = [
    path('', include(router.urls)),
]
