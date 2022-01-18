from django.urls import path, include
from . views import ResturantRegisterApplicationView, MenuView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api-menu/', MenuView, basename='menu')

urlpatterns =[
    path('', include(router.urls)),
    path('api-resturant/', ResturantRegisterApplicationView.as_view(), name='resturant'),
]
