from rest_framework.permissions import BasePermission
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser, GroupEnum


class AlienPermission(BasePermission):
    message = _('User has no admin profile or role.')

    def has_permission(self, request, view):
        user = request.user
        if user.is_blocked:
            self.message = _('User is banned!')
            return False
        user = CustomUser.objects.filter(id=user.id).first()
        admin = user.groups.filter(name=GroupEnum.Alien.value)
        if admin:
            return True
        else:
            return False
