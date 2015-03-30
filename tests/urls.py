"""URL conf for testing Expiring Tokens."""
from django.conf.urls import patterns

from tests.views import MockView

urlpatterns = patterns(
    '',
    (r'^view/$', MockView.as_view()),
)
