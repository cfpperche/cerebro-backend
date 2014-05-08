# coding: utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.utils.translation import ugettext as _

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

class TenantView(TemplateView):
    template_name = "core/tenant.html"