# coding: utf-8

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from cerebromix.core.managers import LogicalDeletedManager
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):

    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """

    deleted = models.BooleanField(default=False, editable=True)
    deleted_at = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now=True)
    deleted_by = models.ForeignKey(
        User, null=True, default=None, editable=False, related_name="%(class)s_deleted")

    created_at = models.DateTimeField(
        default=datetime.now, editable=False, auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, default=None, editable=False, related_name="%(class)s_created")

    updated_at = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now=True)
    updated_by = models.ForeignKey(
        User, null=True, default=None, editable=False, related_name="%(class)s_updated")

    objects = LogicalDeletedManager()
    all_objects = models.Manager()


    def save(self, *args, **kwargs):
        if 'current_user' in kwargs:
            current_user = kwargs.pop("current_user")

            if not self.id:
                self.created_by = current_user

            self.updated_by = current_user

        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        Soft delete all fk related objects that
        inherit from logicaldelete class
        '''

        # Fetch related models
        related_objs = [relation.get_accessor_name() for
                        relation in self._meta.get_all_related_objects()]

        for objs_model in related_objs:
            # Retrieve all related objects
            try:
                obj = getattr(self, objs_model)
            except ObjectDoesNotExist, AttributeError:
                # The attribute  or relation  may not
                # be instanciated.
                pass

            # Checking if inherits from logicaldelete
            if not issubclass(obj.__class__, Model):
                break
            obj.delete()

        # Soft delete the object
        self.deleted = True
        self.save()

    class Meta:
        abstract = True
