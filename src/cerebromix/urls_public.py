#coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cerebromix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    # url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^customer/', include('cerebromix.customers.urls', namespace='customers')),
    url(r'^plan/', include('cerebromix.plans.urls', namespace='plans')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cerebromix.website.urls', namespace='website')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )