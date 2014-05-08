#coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cerebromix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('cerebromix.core.urls', namespace='core')),
    url(r'', include('cerebromix.core.urls', namespace='core')),
)
