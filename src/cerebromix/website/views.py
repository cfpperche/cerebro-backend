# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['about_us'] = _(u'About Us')
        context['features'] = _(u'Features')
        context['recent_projects'] = _(u'Recent Projects')
        context['pricing'] = _(u'Pricing')
        context['our_clients'] = _(u'Our Clients')
        context['ready_to_start'] = _(u'Ready to start your proyect?')

        return context
