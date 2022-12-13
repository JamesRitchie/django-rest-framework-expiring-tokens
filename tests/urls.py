"""URL conf for testing Expiring Tokens."""
from django.urls import re_path

from rest_framework_expiring_authtoken.views import obtain_expiring_auth_token

urlpatterns = [
    re_path(r'^obtain-token/$', obtain_expiring_auth_token),
]
