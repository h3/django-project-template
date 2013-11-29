# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from dajaxice.core import dajaxice_autodiscover
#dajaxice_autodiscover()

admin.autodiscover()

#js_info_dict = {'packages': ('django.conf',),}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
   #(r'^jsi18n$', 'django.views.i18n.javascript_catalog', js_info_dict),
   #(r'^grappelli/', include('grappelli.urls')),
   #(r'^dajaxice/', include('dajaxice.urls')),
   #url(r'^favicon.ico$', RedirectView.as_view(
   #url='%swebsite/img/favicon.ico' % settings.STATIC_URL)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEV:
    urlpatterns += patterns('',
        (r'^%s(.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)
