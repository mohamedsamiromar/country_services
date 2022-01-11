from location.models import *
from django.conf import settings
from accounts.models import Country, BaseModel
from location.models import CurrentLocation


class ResturantRegisterApplication(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True, )
    user_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    location = models.ForeignKey(CurrentLocation,
                                 on_delete=models.CASCADE,
                                 default=False, null=True, blank=False)
    start_working = models.DateTimeField(null=True, blank=True)
    end_working = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(
        choices=(
            (200, 'New'),
            (201, 'Approved'),
            (400, 'Rejected'),
        ), default=200
    )


class ResturantProfile(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True, default=False)
    address = models.CharField(max_length=155, null=True, blank=True, default=False)
    email = models.EmailField(unique=True, null=True, blank=True, default=False)
    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             null=True, blank=True, default=False)
    city = models.CharField(max_length=75, null=True, blank=True, default=False)
    country = models.CharField(max_length=75, null=True, blank=True, default=False)
    occupied_table = models.IntegerField(null=True, blank=True, default=False)
    available_table = models.IntegerField(null=True, blank=True, default=False)
    status = models.CharField(max_length=155, choices=(
        (201, 'Open'),
        (405, 'Closed'),
    ), default='Open')


class Menu(BaseModel):
    pass


class DelivaryOrder(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    resturant = models.ForeignKey(ResturantProfile,
                                  on_delete=models.CASCADE, null=True, blank=True)
    order_count = models.IntegerField(null=True, blank=True)
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)


class ResturantBookingTable(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_mobile_number = models.CharField(max_length=11, null=True, blank=True)
    table_booking_number = models.IntegerField(null=True, blank=True)
    chair_booking_number = models.IntegerField(null=True, blank=True)
    booking_hourse = models.CharField(max_length=150, null=True, blank=True)
