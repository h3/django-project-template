"""
WSGI config for {{ project_name }} project.
"""

import os, sys 

PROJECT_NAME = '{{ project_name }}'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_NAME)
DOC_ROOT = os.path.realpath(os.path.join(\
        os.path.dirname(os.path.abspath(__file__)), '../'))
VIRTUALENVPATH = os.path.join(DOC_ROOT, 'virtualenv/')
PYTHONPATH = [DOC_ROOT, os.path.join(DOC_ROOT, PROJECT_NAME)]

SRC_PATH = os.path.join(DOC_ROOT, '.duke/src/')
for l in os.listdir(SRC_PATH):
    p = os.path.join(SRC_PATH, l)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, 'setup.py')):
        PYTHONPATH.append(p)

EGGS_PATH = os.path.join(DOC_ROOT, '.duke/eggs/')
for l in os.listdir(EGGS_PATH):
    p = os.path.join(EGGS_PATH, l)
    if os.path.isdir(p) and p.endswith('.egg'):
        PYTHONPATH.append(p)

sys.path[0:0] = PYTHONPATH

# USING VIRTUALENV + BUILDOUT

if os.path.exists(VIRTUALENVPATH):
    # http://code.google.com/p/modwsgi/wiki/VirtualEnvironments
    # Remember original sys.path.
    prev_sys_path = list(sys.path)

    # Add site-packages directory.
    for version in ['2.7', '2.6', '2.5']:
        new_site_dir = os.path.join(VIRTUALENVPATH, 'lib/python%s/site-packages/' % version)
        if os.path.exists(new_site_dir):
            site.addsitedir(new_site_dir)
            break

    # Add project's paths
    if path not in sys.path:
        sys.path.append(path)
        sys.path.append(os.path.join(path, PROJECT_NAME))
        contrib = os.path.join(path, 'contrib/')
        if os.path.exists(contrib):
            sys.path.append(contrib)

    # Reorder sys.path so new directories at the front.
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
