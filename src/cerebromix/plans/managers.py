# coding: utf-8

from django.db import models


class PlanPricingManager(models.Manager):

    def get_query_set(self):
        return super(PlanPricingManager, self).get_query_set().select_related('plan', 'pricing')


class PlanQuotaManager(models.Manager):

    def get_query_set(self):
        return super(PlanQuotaManager, self).get_query_set().select_related('plan', 'quota')


class InvoiceManager(models.Manager):

    def get_query_set(self):
        return super(InvoiceManager, self).get_query_set().filter(type=Invoice.INVOICE_TYPES['INVOICE'])


class InvoiceProformaManager(models.Manager):

    def get_query_set(self):
        return super(InvoiceProformaManager, self).get_query_set().filter(type=Invoice.INVOICE_TYPES['PROFORMA'])


class InvoiceDuplicateManager(models.Manager):

    def get_query_set(self):
        return super(InvoiceDuplicateManager, self).get_query_set().filter(type=Invoice.INVOICE_TYPES['DUPLICATE'])
