from allauth.socialaccount import providers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings


@api_view(['GET'])
@permission_classes([AllowAny])
def get_facebook_url(request):
    provider = providers.registry.by_id('facebook', None)
    path = provider.get_login_url(request)
    url = settings.MY_APP_URL + path
    return Response({'url': url})
