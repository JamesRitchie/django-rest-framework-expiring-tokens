"""Expiring Token models.

Classes:
    ExpiringToken
"""

from django.conf import settings
from django.utils import timezone

from rest_framework.authtoken.models import Token


class ExpiringToken(Token):

    """Extend Token to add an expired method."""

    class Meta(object):
        proxy = True

    def expired(self):
        """Return boolean indicating token expiration."""
        now = timezone.now()
        if self.created < now - settings.EXPIRING_TOKEN_LIFESPAN:
            return True
        return False

    def expiration_set(self):
        """Return boolean indicating if EXPIRING_TOKEN_LIFESPAN has been set in projects setting.py file"""
        try:
            settings.EXPIRING_TOKEN_LIFESPAN
            return True
        except AttributeError:
            return False