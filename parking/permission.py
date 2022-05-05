from rest_framework.permissions import IsAuthenticated, BasePermission
from django.utils.translation import ugettext_lazy as _
from parking.models import ParkingProfile


class ParkingAccess(BasePermission):
    message = _('User has no access to this corporate.')

    def has_permission(self, request, view):
        user = request.user
        if user.is_blocked:
            self.message = _('User is banned!')
            return False
        try:
            if user.groups.filter(name='Parking').exists() and user.corporateemployeeprofile:
                return True
            return False
        except ParkingProfile.DoesNotExist:
            return False
