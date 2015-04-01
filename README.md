# Expiring Tokens for Django Rest Framework

[![Build Status](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens.svg?branch=master)](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens)
[![Coverage Status](https://coveralls.io/repos/JamesRitchie/django-rest-framework-expiring-tokens/badge.svg)](https://coveralls.io/r/JamesRitchie/django-rest-framework-expiring-tokens)
[![Code Health](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master/landscape.svg?style=flat)](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master)

This package provides a lightweight extension to the included Token
authentication in Django Rest Framework, causing tokens to expire after
a specified duration.

This behaviour is good practice when using token authentication for production
APIs.
If you require more complex token functionality, you're probably better off
looking at one of the OAuth2 implementations available for Django Rest
Framework.

This package was inspired by this
[Stack Overflow answer](http://stackoverflow.com/a/15380732).

## Installation

Grab the package from PyPI.

```zsh
pip install --pre djangorestframework-expiring-tokens
```

As this package uses a proxy model on the original Token model, the first step
is to setup the default
[TokenAuthentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
scheme, and check that it works.

Then, add the package to `INSTALLED_APPS` along with `rest_framework.authtoken` in `settings.py`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_expiring_authtoken',
    ...
]
```

Specify the desired lifespan of a token with `EXPIRING_TOKEN_LIFESPAN` in
`settings.py` using a
[timedelta object](https://docs.python.org/2/library/datetime.html#timedelta-objects).

```python
import datetime
EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=30)
```

[Set the authentication scheme](http://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme) to `rest_framework_expiring_authtoken.authentication.ExpiringTokenAuthentication`
on a default or per-view basis.

If you used the `obtain_auth_token` view, you'll need to replace it with the  `obtain_expiring_auth_token` view in your URLconf.

```python
from rest_framework_expiring_authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_expiring_auth_token)
]
```

## Usage

Expiring Tokens works exactly the same as the default TokenAuth, except that using an expired token will return a response with an HTTP 400 status and a `Token has expired` error message.

The `obtain_expiring_auth_token` view works exactly the same as the `obtain_auth_token` view, except it will replace existing tokens that have expired with a new token.

## Improvements

 * Potentially have a default setting for token lifespan.
 * Variable token lifespans.
 * Possibly change `obtain_expiring_auth_token` to always replace an existing token. (Configurable?)
 * South Migrations
