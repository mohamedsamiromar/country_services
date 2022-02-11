from rest_framework import permissions, status
from alien.models import Alien


class AlienAccountAccess(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if Alien.objects.filter(user=request.user).exists():
            return True
        return False