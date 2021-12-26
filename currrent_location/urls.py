from django.urls import path
from currrent_location import views as current_view
from django_restful_admin import admin as api_admin

urlpatterns = [
    path('apiadmin/', api_admin.site.urls),
    path('current_location', current_view.current_location_view, name='get_current_location'),
]