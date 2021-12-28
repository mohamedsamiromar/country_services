from django.urls import path
from . views import ResturantRegisterApplicationView

urlpatterns =[
    path('resturant', ResturantRegisterApplicationView.as_view(), name='resturant')
]