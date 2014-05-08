#coding: utf-8

from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    """
    A base model admin to use in providing access to to logically deleted
    objects.
    """
    
    list_display = ('created_at', 'updated_at', "deleted",)

    list_filter = ('created_at','updated_at','deleted',)
 
    date_hierarchy = 'created_at'
 
    search_fields = ('created_at', 'updated_at',)


    def queryset(self, request):
        """ Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view. """
        # Default: qs = self.model._default_manager.get_query_set()
        qs = self.model._default_manager.all_with_deleted()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.ordering or () # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

