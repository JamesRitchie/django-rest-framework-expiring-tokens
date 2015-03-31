# Expiring Tokens for Django Rest Framework

[![Build Status](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens.svg?branch=master)](https://travis-ci.org/JamesRitchie/django-rest-framework-expiring-tokens)
[![Coverage Status](https://coveralls.io/repos/JamesRitchie/django-rest-framework-expiring-tokens/badge.svg)](https://coveralls.io/r/JamesRitchie/django-rest-framework-expiring-tokens)
[![Code Health](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master/landscape.svg?style=flat)](https://landscape.io/github/JamesRitchie/django-rest-framework-expiring-tokens/master)

This package provides a lightweight extension to the included Token
authentication in Django Rest Framework, causing tokens to expire after
a specified duration.
This behaviour is good practice when using token authentication for production
APIs.
Inspired by this Stack Overflow [answer](http://stackoverflow.com/a/15380732).

## Installation

As this package uses a proxy model on the original Token model, the first step
is to setup the default [TokenAuthentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) scheme, and check that it works.

Then, add the package to `INSTALLED_APPS` along with `rest_framework.authtoken` in `settings.py`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
    'rest_framework_expiring_authtoken',
    ...
```

Specify the desired lifespan of a token with `EXPIRING_TOKEN_LIFESPAN` in
`settings.py` using a
[timedelta](https://docs.python.org/2/library/datetime.html#timedelta-objects)
object.

```python
import datetime
EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=30)
```

[Set the authentication scheme](http://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme) to `rest_framework_expiring_authtoken.authentication.ExpiringTokenAuthentication`
on a default or per-view basis.
