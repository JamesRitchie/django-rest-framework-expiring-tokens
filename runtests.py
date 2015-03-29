#!/usr/bin/env python
import os
import sys


def run():
    """Run tests with Django setup."""
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    from django.conf import settings

    # Will only work in 1.7
    try:
        from django import setup
    except ImportError:
        pass
    else:
        setup()

    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))

if __name__ == "__main__":
    run()
