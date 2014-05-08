# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, ugettext as _
from cerebromix.core.admin import BaseAdmin
from cerebromix.customers.models import Client


class CustomerAdmin(BaseAdmin):

    list_display = ('name',) + BaseAdmin.list_display

    search_fields = ('name',) + BaseAdmin.search_fields
    
    list_filter = ('name',) + BaseAdmin.list_filter

    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'created_by', None) is None:
    #         obj.created_by = request.user
    #     else
    #         obj.updated_by = request.user

    #     obj.save()
    
admin.site.register(Client, CustomerAdmin)
