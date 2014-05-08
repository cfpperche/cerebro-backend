# coding: utf-8
from django.conf.urls import patterns, include, url
from cerebromix.customers.views import SignInView

urlpatterns = patterns('cerebromix.customers.views',
    #url(r'^signin/', SignInView.as_view(), name='signin'),
	url(r'^signin/$', 'entrar', name='signin'),
    url(r'^signout/$', 'sair', name='signout'),
)
