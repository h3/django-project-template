# -*- coding: utf-8 -*-

# Django settings for {{ project_name }} project.

import os

PROJECT_PATH = os.path.realpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../'))

DEV = DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

ADMINS = (
    ('Maxime Haineault', 'max@motion-m.ca'),
)

MANAGERS = ADMINS

DATABASE_ROUTERS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}.db',
    }
}

DATABASE_OPTIONS = {
    'use_unicode': True,
    'charset': 'utf8',
}

# Admin

GRAPPELLI_ADMIN_TITLE = 'Administration'
#GRAPPELLI_INDEX_DASHBOARD = '{{ project_name }}.dashboard.CustomIndexDashboard'

# Emails

#EMAIL_HOST = 'smtp.site.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'user@name.com'
#EMAIL_HOST_PASSWORD = '******'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = '"Full Name" <%s>' % EMAIL_HOST_USER
#DEFAULT_EMAIL_RECIPIENTS = ['to@email.com']


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-ca'

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext(u'English')),
   #('fr', gettext(u'Francais')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.realpath(os.path.join(PROJECT_PATH, '../../static/'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   #'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.humanize',
   #'grappelli',
   #'grappelli.dashboard',
   #'grappellifit',
    'django.contrib.admin',
    'south',
   #'easy_thumbnails',
   #'crispy_forms',
   #'dajaxice',
   #'filebrowser',
   #'easy_thumbnails',
   #'crispy_forms',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
       #'dajaxice': {
       #    'handlers': ['console'],
       #    'level': 'WARNING',
       #    'propagate': False,
       #},
       #'xhtml2pdf': {
       #    'handlers': ['console'],
       #    'level': 'WARNING',
       #    'propagate': False,
       #},
    }
}

#LOGIN_REDIRECT_URL = '/admin/'

#CSRF_FAILURE_VIEW = 'website.views.error_403'

#handler500 = 'website.views.error_500'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SOUTH_TESTS_MIGRATE = False
DEFAULT_FILE_STORAGE = '{{ project_name }}.utils.ASCIISafeFileSystemStorage'

# easy_thumbnails: store into media/cache/ instead of polluting media/uploads/
THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'cache/')
THUMBNAIL_MEDIA_URL = '/media/cache/'

CRISPY_TEMPLATE_PACK = 'bootstrap' # Defaults, but tests fails if not set..

#AUTH_USER_MODEL = 'myapp.User'

# Filebrowser
#FILEBROWSER_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'assets/')
#FILEBROWSER_MEDIA_URL = MEDIA_URL + 'assets/'
#FILEBROWSER_DIRECTORY = ''
#
#FILEBROWSER_VERSIONS = {
#    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
#    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
#    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
#    'medium': {'verbose_name': 'Medium (6col )', 'width': 460, 'height': '', 'opts': ''},
#    'big': {'verbose_name': 'Big (8 col)', 'width': 610, 'height': '', 'opts': ''},
#    'large': {'verbose_name': 'Large (9 col)', 'width': 700, 'height': '', 'opts': ''},
#}
