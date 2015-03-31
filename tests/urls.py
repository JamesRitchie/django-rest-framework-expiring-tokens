"""URL conf for testing Expiring Tokens."""
from django.conf.urls import patterns

from rest_framework_expiring_authtoken.views import obtain_expiring_auth_token

urlpatterns = patterns(
    '',
    (r'^obtain-token/$', obtain_expiring_auth_token),
)
