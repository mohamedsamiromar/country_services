from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('alien/token/', views.AlienTokenObtainPairView.as_view()),
    path('parking/token/', views.ParkingTokenObtainPairView.as_view()),
    path('restaurant/token/', views.ResturantTokenObtainPairView.as_view()),
    path('pharmacy/token/', views.PharmacyTokenObtainPairView.as_view()),
    path('hotel/token/', views.HotelTokenObtainPairView.as_view()),
]
