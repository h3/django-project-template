# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

#from dajaxice.core import dajaxice_autodiscover

admin.autodiscover()
#dajaxice_autodiscover()

#js_info_dict = {'packages': ('django.conf',),}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^i18n/',      include('django.conf.urls.i18n')),
   #(r'^jsi18n$',       'django.views.i18n.javascript_catalog', js_info_dict),
   #(r'^grappelli/', include('grappelli.urls')),
   #(r'^dajaxice/', include('dajaxice.urls')),
   #(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {
   #    'url': '%swebsite/img/favicon.ico' % settings.STATIC_URL}),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEV:
    urlpatterns += patterns('',
        (r'^%s(.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)
