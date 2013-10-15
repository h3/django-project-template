import os

from %(project)s.conf.settings.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '%(project)s_db',
        'USER': '%(project)s',
        'PASSWORD': '',
    }
}

#EMAIL_HOST = 'smtp.server.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'email@server.com'
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True 
#DEFAULT_FROM_EMAIL = '"Firstname Lastname" <%s>' % EMAIL_HOST_USER

#SENTRY_DSN = ''

MEDIA_ROOT = '/var/www/medias/prod/'
#THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'cache/')
