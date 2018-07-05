# !/usr/bin/env python
# coding: utf8

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from PDI.core_1.views import deteccao

admin.autodiscover()

urlpatterns = ['',
               url(r'^deteccao/', 'PDI.core_1.views.deteccao', name='deteccao'),
               url(r'^admin/', admin.site.urls)]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
