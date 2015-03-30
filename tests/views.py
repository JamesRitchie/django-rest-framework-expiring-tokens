"""
Views used for testing Expiring Tokens.

Classes:
    MockView: Test view.
"""
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework_expiring_authtoken import ExpiringTokenAuth


class MockView(APIView):

    """Mock APIView for testing."""

    authentication_classes = (ExpiringTokenAuth,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Return JSON string to GET request."""
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def post(self, request):
        """Return JSON string to POST request."""
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def put(self, request):
        """Return JSON string to PUT request."""
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})
