from django.urls import path
from . views import ResturantRegisterApplicationView, \
                    GetResturantRegisterApplicationView

urlpatterns =[
    path('resturant', ResturantRegisterApplicationView.as_view(), name='resturant'),
    path('get_resturant', GetResturantRegisterApplicationView.as_view(), name='get_resturant')
]
