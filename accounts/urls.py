
from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('alien/token/', views.AlienTokenObtainPairView.as_view()),
    path('parking/token/', views.ParkingTokenObtainPairSerializer.as_view()),
    path('restaurant/token/', views.RestaurantTokenObtainPairSerializer.as_view()),
    path('pharmacy/token/', views.PharmacyTokenObtainPairView.as_view()),
    path('hotel/token/', views.HotelTokenObtainPairSerializer.as_view()),
]
