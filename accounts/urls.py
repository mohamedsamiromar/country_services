
from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('alien/token/', views.AlienTokenObtainPairView.as_view()),
]
