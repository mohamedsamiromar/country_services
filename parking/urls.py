from django.urls import path, include
from parking import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('parking-profile/', views.ParkingView.as_view()),
    path('booking-parking/', views.BookingParkingView.as_view()),
    path('parking-status/', views.ParkingFullAndNotFull.as_view()),
]
