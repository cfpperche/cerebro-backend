# coding: utf-8
from django.conf.urls import patterns, include, url
from cerebromix.website.views import HomeView

urlpatterns = patterns('cerebromix.website.views',
    url(r'^$', HomeView.as_view(), name='home'),
    
)