# coding: utf-8

from django.db import models

from cerebromix.core.query import LogicalDeleteQuerySet

class LogicalDeletedManager(models.Manager):
    """
    A manager that serves as the default manager for `logicaldelete.models.Model`
    providing the filtering out of logically deleted objects.  In addition, it
    provides named querysets for getting the deleted objects.
    """
    
    def get_query_set(self):
        if self.model:
            return LogicalDeleteQuerySet(self.model, using=self._db).filter(
                deleted=False
            )
    
    def all_with_deleted(self):
        if self.model:
            return super(LogicalDeletedManager, self).get_query_set()
    
    def only_deleted(self):
        if self.model:
            return super(LogicalDeletedManager, self).get_query_set().filter(
                deleted=False
            )
    
    def get(self, *args, **kwargs):
        return self.all_with_deleted().get(*args, **kwargs)
    
    def filter(self, *args, **kwargs):
        if "pk" in kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_query_set().filter(*args, **kwargs)