"""URL conf for testing Expiring Tokens."""
from django.conf.urls import url

from rest_framework_expiring_authtoken.views import obtain_expiring_auth_token

urlpatterns = [
    url(r'^obtain-token/$', obtain_expiring_auth_token),
]
