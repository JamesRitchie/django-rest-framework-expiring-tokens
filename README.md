# Expiring Tokens for Django Rest Framework

[![Build Status](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens.svg?branch=master)](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens)
[![Coverage Status](https://coveralls.io/repos/JamesRitchie/django-rest-framework-expiring-tokens/badge.svg)](https://coveralls.io/r/JamesRitchie/django-rest-framework-expiring-tokens)
[![Code Health](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master/landscape.svg?style=flat)](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master)
[![PyPI version](https://badge.fury.io/py/djangorestframework-expiring-authtoken.svg)](http://badge.fury.io/py/djangorestframework-expiring-authtoken)
[![Requirements Status](https://requires.io/github/JamesRitchie/django-rest-framework-expiring-tokens/requirements.svg?branch=master)](https://requires.io/github/JamesRitchie/django-rest-framework-expiring-tokens/requirements/?branch=master)

This package provides a lightweight extension to the included token
authentication in
[Django Rest Framework](http://www.django-rest-framework.org/), causing tokens
to expire after a specified duration.

This behaviour is good practice when using token authentication for production
APIs.
If you require more complex token functionality, you're probably better off
looking at one of the OAuth2 implementations available for Django Rest
Framework.

This package was inspired by this
[Stack Overflow answer](http://stackoverflow.com/a/15380732).

## Installation

Expiring Tokens is tested against the latest versions of Django 1.6, 1.7 and
the 1.8 preview release, and Django Rest Framework 3.1.1.
It should in theory support Django 1.4.

Grab the package from PyPI.

```zsh
pip install djangorestframework-expiring-authtoken
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
If not set, the default is 30 days.

```python
import datetime
EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=25)
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

If using Django 1.7 or later, you'll need to run `migrate`, even though nothing
is changed, as Django requires proxy models that inherit from models in an
app with migrations to also have migrations.

```zsh
python manage.py migrate
```

## Usage

Expiring Tokens works exactly the same as the default TokenAuth, except that using an expired token will return a response with an HTTP 400 status and a `Token has expired` error message.

The `obtain_expiring_auth_token` view works exactly the same as the `obtain_auth_token` view, except it will replace existing tokens that have expired with a new token.

## Improvements

 * Variable token lifespans.
 * Possibly change `obtain_expiring_auth_token` to always replace an existing token. (Configurable?)
 * South Migrations

## Contributors

 * [James Ritchie](https://github.com/JamesRitchie)
 * [fcasas](https://github.com/fcasas)

## Changelog

 * 0.1.4
  * Fixed a typo causing an incorrect 500 error response with an invalid token.
  * Support Django 1.10 and Django Rest Framework 3.4
 * 0.1.3
  * Set a default token lifespan of 30 days.
 * 0.1.2
  * Changed from deprecated `request.DATA` to `request.data`
 * 0.1.1
  * Initial release
