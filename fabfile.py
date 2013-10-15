import os
from fabric.api import *
from fabric.contrib import files

from dukeclient.fabric.utils import get_role, get_conf, get_project_path
from dukeclient.fabric.tasks import *

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

env.roledefs.update({
    'alpha': ['user@alpha.myproject.com'],
    'beta': ['user@beta.myproject.com:2022'],
    'prod': ['user@myproject.com'],
})

env.site = {
    'domain':   'myproject.com',
    'package':  'my-project',
    'project':  'myproject',
    'repos':    'git+git@gitserver.com:user/my-project.git',
}

env.roleconfs = {}

# Example config using UWSGI with Supervisor behind Nginx

env.roleconfs['prod'] = {
    'hosts': env.roledefs['prod'],
    'user': 'www-data',
    'group': 'www-data',
    'document-root':    '/var/www/vhosts/%(domain)s/',
    'media-root':       '/var/www/vhosts/%(domain)s/media',
    'static-root':      '/var/www/vhosts/%(domain)s/static',
    'vhost-conf':       '/etc/nginx/sites-available/%(domain)s',
    # Unless you are not using dajaxice, you want to use static-copy.
    # https://github.com/jorgebastida/django-dajaxice/issues/66
    'static-copy': True,
    'virtualenv': True,
    'virtualenv-root': '/var/www/vhosts/%(domain)s/virtualenv/clientsbp',
    'on-deploy': [
        'mkdir -p /var/www/vhosts/%(domain)s/media/',
    ],
    'on-deploy-done': [
        'ln -sf /etc/nginx/sites-available/%(domain)s /etc/nginx/sites-enabled/%(domain)s',
        'ln -sf /var/www/vhosts/%(domain)s/%(package)s/deploy/prod.%(domain)s.ini /etc/uwsgi/apps-enabled/%(domain)s.ini',
        'ln -sf /var/www/vhosts/%(domain)s/%(package)s/deploy/prod_supervisord.conf /etc/supervisor/conf.d/clients.%(domain)s.conf',
        'touch /etc/uwsgi/apps-enabled/%(domain)s.ini',
        '/etc/init.d/nginx reload',
        'supervisorctl reread && supervisorctl restart %(package)s',
    ],
}

# Example config for Plesk

env.roleconfs['beta'] = {
    'hosts': env.roledefs['beta'],
    'user': 'ncXXXXX',
    'group': 'psaserv',
    'document-root': '/var/www/vhosts/%(domain)s/httpdocs/',
    'media-root':  '/var/www/vhosts/%(domain)s/httpdocs/media/',
    'static-root': '/var/www/vhosts/%(domain)s/httpdocs/static/',
    'vhost-conf': '/var/www/vhosts/%(domain)s/conf/vhost.conf',
    'wsgi-processes': 1,
    'wsgi-threads': 5,
    'virtualenv': True,
    'static-copy': True,
    'on-apache-reload': [
        '/usr/local/psa/admin/sbin/websrvmng --reconfigure-vhost --vhost-name=%(domain)s',
    ],
    'on-deploy-done': [
        'ln -sf /var/www/vhosts/%(domain)s/httpdocs/%(domain)s/%(project)s/media /var/www/vhosts/%(domain)s/httpdocs/media',
    ],
}

# Example config for CPanel. But seriously, don't host any django on CPanel. It
# will ruin your life and leave you with PTSD. Seriously. Don't.

env.roleconfs['alpha'] = {
    'hosts': env.roledefs['alpha'],
    'user': 'ncXXXXX',
    'group': 'ncXXXXX',
    'document-root': '/home/ncXXXXX/public_html/',
    'media-root': '/home/ncXXXXX/public_html/media/',
    'static-root': '/home/ncXXXXX/public_html/static/',
    # You will have to do some preparation on the server, like activating
    # dynamic virtual hosts. Good luck with that.
    'vhost-conf': '/usr/local/apache/conf/userdata/std/2/ncXXXXX/%(domain)s/vhost.conf',
    'virtualenv': True,
    'static-copy': True,
    'on-deploy': [
        # CPHulk will blacklist your user systematically after a certain amount
        # of sudo, regardless if your script disconnect/reconnect or not. Fail.
        '/usr/local/cpanel/bin/cphulk_pam_ctl --disable',
        # One have to respect the conciseness and implacable logic of
        # CPanel's choice of directory structure..
        'mkdir -p /usr/local/apache/conf/userdata/std/2/ncXXXXX/%(domain)s',
    ],
    'on-deploy-done': [
        'sudo /scripts/verify_vhost_includes',
        'sudo /scripts/ensure_vhost_includes --user=ncXXXXX',
        'ln -sf /home/ncXXXXX/public_html/%(domain)s/%(project)s/media /home/ncXXXXX/public_html/media',
        # Here we re-enable our friendly fire prone buddy (CPHulk)
        '/usr/local/cpanel/bin/cphulk_pam_ctl --enable',
        # The Frontpage extension will fuck randomly with your .htaccess every
        # now and then.. the only reliable workaround I've found is to
        # unsetup/setup it.
        '/scripts/unsetupfp4 %(domain)s && /scripts/setupfp4 %(domain)s',
    ],
    'wsgi-processes': 1,
    'wsgi-threads': 5,
}
