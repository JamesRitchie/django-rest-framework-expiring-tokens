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
    def EXPIRING_TOKEN_SLIDE_WINDOW(self):
        """
        Returns the time window for sliding a token's expiration.
        Defaults to 0 milliseconds i.e. no sliding enabled.
        """
		
        try:
            val = settings.EXPIRING_TOKEN_SLIDE_WINDOW
        except AttributeError:
            val = timedelta(milliseconds=0)

        return val

token_settings = TokenSettings()
