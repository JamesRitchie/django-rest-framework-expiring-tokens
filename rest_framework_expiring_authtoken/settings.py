"""
Provides access to settings.

Returns defaults if not set.
"""
from datetime import timedelta

from django.conf import settings


class TokenSettings(object):

    """Provides settings as defaults for working with tokens."""

    @property
    def EXPIRING_TOKEN_LIFESPAN(self):
        """
        Return the allowed lifespan of a token as a TimeDelta object.

        Defaults to 30 days.
        """
        try:
            val = settings.EXPIRING_TOKEN_LIFESPAN

        except AttributeError:
            val = timedelta(days=30)

        return val

    @property
    def ALWAYS_RESET_TOKEN(self):
        """
        Return if token should be reset every time at login

        Defaults to False
        """
        try:
            val = settings.ALWAYS_RESET_TOKEN

        except AttributeError:
            val = False

        return val

token_settings = TokenSettings()
