# -*- coding: utf-8 -*-

# Django settings entry point for {{ project_name }} project.

"""
WARNING: YOU SHOULD NOT HAVE TO EDIT THIS FILE.

http://justcramer.com/2011/01/13/settings-in-django/

To configure your site, modify one of the following files:

 * ./local_settings.py

   This settings extends dev.py and is used to develop the project. This file
   is specific to each developers/machines your project is being developed on.
   So it should not be added to your VCS.

 * ./conf/settings/dev.py

   This settings contains settings specific to the development environment.
   For example: DEBUG = True. If the settings you want to set is specific to
   you or the machine you are working on, it should instead be set in
   local_settings.py

 * ./conf/settings/default.py

   This is the main settings files. It should contain the default settings of
   your project. The one that are used in production that is.

"""

import os

## Import our defaults (globals)

from {{ project_name }}.conf.settings.default import *

## Inherit from environment specifics

DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

## Import local settings

try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("""
Warning: Can't find the file 'local_settings.py' in the directory containing
%r. It appears you've customized things.\nYou'll have to run django-admin.py,
passing it your settings module.\n(If the file settings.py does indeed exist,
it's causing an ImportError somehow.)\n""" % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()

## Remove disabled apps

if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    DATABASE_ROUTERS = list(DATABASE_ROUTERS)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)

        for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
            if m.startswith(a):
                TEMPLATE_CONTEXT_PROCESSORS.pop(x)

        for x, m in enumerate(DATABASE_ROUTERS):
            if m.startswith(a):
                DATABASE_ROUTERS.pop(x)
