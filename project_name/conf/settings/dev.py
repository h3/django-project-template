# -*- coding: utf-8 -*-

# Development environment settings

import os, getpass

from {{ project_name }}.conf.settings.default import *

DEV = True
DEBUG = True
DJANGO_NOSE = False

TEMPLATE_LOADERS = (
    # Remove cached template loader
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

DISABLED_APPS = ['raven', 'sentry']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/')

THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'cache/')
THUMBNAIL_MEDIA_URL = '/media/cache/'

DATABASE_PREFIX = ''
DATABASE_USER = getpass.getuser()
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = None

for k, v in DATABASES.iteritems():
    DATABASES[k].update({
        'NAME': DATABASE_PREFIX + v['NAME'],
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'OPTIONS': {
            'autocommit': False
        }
    })

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'CACHE+' + SECRET_KEY
    }
}

# django-devserver: http://github.com/dcramer/django-devserver
try:
    import devserver
except ImportError:
    pass
else:
    INSTALLED_APPS = INSTALLED_APPS + ('devserver',)
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('devserver.middleware.DevServerMiddleware',)
    DEVSERVER_IGNORED_PREFIXES = ['/media', '/static']
    DEVSERVER = True

# TESTS

if DJANGO_NOSE:
    INSTALLED_APPS = INSTALLED_APPS + ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
