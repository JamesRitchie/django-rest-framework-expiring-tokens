"""Tests for Expiring Tokens authentication class."""
from datetime import timedelta
from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework_expiring_authtoken.authentication import (
    ExpiringTokenAuthentication
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_expiring_authtoken.models import ExpiringToken


class ExpiringTokenAuthenticationTestCase(TestCase):

    """Test the authentication class directly."""

    def setUp(self):
        """Create a user and associated token."""
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

        self.key = 'abc123'
        self.token = ExpiringToken.objects.create(
            user=self.user,
            key=self.key
        )

        self.test_instance = ExpiringTokenAuthentication()

    def test_valid_token(self):
        """Check that a valid token authenticates correctly."""
        result = self.test_instance.authenticate_credentials(self.key)

        self.assertEqual(result[0], self.user)
        self.assertEqual(result[1], self.token)

    def test_invalid_token(self):
        """Check that an invalid token does not authenticated."""
        try:
            self.test_instance.authenticate_credentials('xyz789')
        except AuthenticationFailed as e:
            self.assertEqual(e.__str__(), 'Invalid token')
        else:
            self.fail("AuthenticationFailed not raised.")

    def test_inactive_user(self):
        """Check that a token for an inactive user cannot authenticate."""
        # Make the user inactive
        self.user.is_active = False
        self.user.save()

        try:
            self.test_instance.authenticate_credentials(self.key)
        except AuthenticationFailed as e:
            self.assertEqual(e.__str__(), 'User inactive or deleted')
        else:
            self.fail("AuthenticationFailed not raised.")

    def test_expired_token(self):
        """Check that an expired token cannot authenticate."""
        # Crude, but necessary as auto_now_add field can't be changed.
        with self.settings(EXPIRING_TOKEN_LIFESPAN=timedelta(milliseconds=1)):
            sleep(0.001)

            try:
                self.test_instance.authenticate_credentials(self.key)
            except AuthenticationFailed as e:
                self.assertEqual(e.__str__(), 'Token has expired')
            else:
                self.fail("AuthenticationFailed not raised.")

    def test_always_reset_token(self):
        """Check that token always expires."""
        with self.settings(ALWAYS_RESET_TOKEN=True):
            sleep(0.001)

            try:
                self.test_instance.authenticate_credentials(self.key)
            except AuthenticationFailed as e:
                self.assertEqual(e.__str__(), 'Token has expired')
            else:
                self.fail("AuthenticationFailed not raised.")
