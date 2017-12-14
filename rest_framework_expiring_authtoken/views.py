"""Utility views for Expiring Tokens.

Classes:
    ObtainExpiringAuthToken: View to provide tokens to clients.
"""
from .serializers import EmailAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from rest_framework_expiring_authtoken.models import ExpiringToken


class ObtainExpiringAuthToken(ObtainAuthToken):

    """View enabling email/password exchange for expiring token."""

    model = ExpiringToken

    def post(self, request):
        """Respond to POSTed email/password with token."""
        serializer = EmailAuthTokenSerializer(data=request.data)

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

            data = {'auth_token': token.key}

            return Response(data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
