from django.urls import path
from . views import ResturantRegisterApplicationView

urlpatterns =[
    path('crea_restorant', ResturantRegisterApplicationView.as_view(), name='resturant'),
]
