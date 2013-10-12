# -*- coding: utf-8 -*-

from {{ project_name }}.conf.settings.dev import *

DEBUG_TOOLBAR = True
DEBUG = True
DEV = True
DEV_SERVER = True
DEBUG_TOOLBAR = False

#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DISABLED_APPS = ['sentry']

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.oracle',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

if DEV_SERVER:
    INSTALLED_APPS = INSTALLED_APPS + ('devserver',)
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('devserver.middleware.DevServerMiddleware',)
    DEVSERVER_MODULES = []
    #  'devserver.modules.sql.SQLRealTimeModule',
    #  'devserver.modules.sql.SQLSummaryModule',
    #  'devserver.modules.profile.ProfileSummaryModule',
    #  'devserver.modules.request.SessionInfoModule',
    #  'devserver.modules.profile.MemoryUseModule',
    #  'devserver.modules.profile.LeftOversModule',
    #  'devserver.modules.cache.CacheSummaryModule',

if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'dev', 'localhost')
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    #HIDE_DJANGO_SQL = True
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
        #'HIDE_DJANGO_SQL': True,
        #'ENABLE_STACKTRACES' : True,
    }
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
       #'debug_toolbar.panels.logger.LoggingPanel',
    )

