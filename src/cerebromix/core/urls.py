# coding: utf-8

from django.conf.urls import patterns, include, url
from cerebromix.core.views import TenantView

#from cerebromix.customers.models import Client
#tenant = Client(domain_url='test1.tenant.com', schema_name='test1', name='test1 tenant')
#tenant.save()

urlpatterns = patterns('cerebromix.core.views',
   	url(r'^$', TenantView.as_view(), name='tenantview'),
)
