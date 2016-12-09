"""Utility views for Expiring Tokens.

Classes:
    ObtainExpiringAuthToken: View to provide tokens to clients.
"""
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import AnonymousUser

from rest_framework_expiring_authtoken.models import ExpiringToken


class ObtainExpiringAuthToken(ObtainAuthToken):

    """View enabling username/password exchange for expiring token."""

    model = ExpiringToken
    authentication_classes = (BasicAuthentication, )
    
    def get(self, request):
        """Respond to GET username/password(Header - HTTP Basic Auth) with token."""

        if request.user and not isinstance(request.user, AnonymousUser):
            token, _ = ExpiringToken.objects.get_or_create(
                user=request.user
            )

            if token.expired():
                # If the token is expired, generate a new one.
                token.delete()
                token = ExpiringToken.objects.create(
                    user=request.user
                )

            data = {'token': token.key}
            return Response(data)

        return Response({'detail': "Couldn't find user"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """Respond to POSTed username/password with token."""
        serializer = AuthTokenSerializer(data=request.data)

        if serializer.is_valid():
            token, _ = ExpiringToken.objects.get_or_create(
                user=serializer.validated_data['user']
            )

            if token.expired():
                # If the token is expired, generate a new one.
                token.delete()
                token = ExpiringToken.objects.create(
                    user=serializer.validated_data['user']
                )

            data = {'token': token.key}
            return Response(data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
