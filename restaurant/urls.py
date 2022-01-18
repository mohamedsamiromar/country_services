from django.urls import path
from . views import ResturantRegisterApplicationView, MenuView

urlpatterns =[
    path('/api-resturant/', ResturantRegisterApplicationView.as_view(), name='resturant'),
    path('/api-menu/', MenuView.as_view(), name='menu'),
]
