from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from accounts.views import AlienTokenObtainPairView, ResturantTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # all auth
    path('auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

    path('auth/registration/', include('rest_auth.registration.urls')),
    path('login', views.obtain_auth_token, name='api_token_auth'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('alien/token/', AlienTokenObtainPairView.as_view(),name='alien_token_obtain_pair'),
    path('resturant/token/', ResturantTokenObtainPairView.as_view(),name='resturant_token_obtain_pair'),

    path('location/', include('location.urls')),
    path('auth/', include('authentication.urls')),
    path('resturant/', include('restaurant.urls')),
    path('alien/', include('alien.urls')),
    path('pharmacy/', include('pharmacy.urls'))

]
