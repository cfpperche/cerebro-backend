# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from cerebromix.tenant_schemas.models import TenantMixin
from cerebromix.tenant_schemas.utils import tenant_context

from cerebromix.core.models import BaseModel


class Client(TenantMixin, BaseModel):

    user = models.OneToOneField('auth.User', verbose_name=_('user'))

    name = models.CharField(_(u'name'), max_length=100)

    class Meta:
        verbose_name = _(u'Client')
        verbose_name_plural = _(u'Clients')

    def __unicode__(self):
        return self.name

    # default true, schema will be automatically created and synced when it is
    # saved
    auto_create_schema = True

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super(Client, self).save(*args, **kwargs)

        if is_new:
            with tenant_context(self):
                User.objects.create_user(
                    self.schema_name, self.schema_name + '@admin.tld', self.schema_name)