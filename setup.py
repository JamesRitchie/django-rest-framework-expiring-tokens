"""Setup file for rest_framework_sav."""
import os
import sys

from setuptools import setup, find_packages

import rest_framework_expiring_authtoken


version = rest_framework_expiring_authtoken.__version__

if sys.argv[-1] == 'publish':
    if os.system("pip list | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='djangorestframework-expiring-authtoken',
    version=version,
    description='Expiring Authentication Tokens for Django REST Framework',
    url=(
        'https://github.com/JamesRitchie/django-rest-framework-expiring-tokens'
    ),
    author='James Ritchie',
    author_email='james.a.ritchie@gmail.com',
    license='BSD',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'djangorestframework>=3.4'
    ],
    test_suite='runtests.run',
    tests_require=[
        'Django>=1.8.14,<2'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
