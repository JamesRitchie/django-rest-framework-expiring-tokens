"""Tests for Expiring Token models.

Classes:
    ExpiringTokenTestCase: Tests ExpiringToken.
"""
from datetime import timedelta
from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework_expiring_authtoken.models import ExpiringToken


class ExpiringTokenTestCase(TestCase):

    """Test case for Expiring Token model."""

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

    def test_expired_indated(self):
        """Check the expired method returns false for an indated token."""
        self.assertFalse(self.token.expired())

    def test_expired_outdated(self):
        """Check the expired method return true for an outdated token."""
        # Crude, but necessary as auto_now_add field can't be changed.
        with self.settings(EXPIRING_TOKEN_LIFESPAN=timedelta(milliseconds=1)):
            sleep(0.003)
            self.assertTrue(self.token.expired())
