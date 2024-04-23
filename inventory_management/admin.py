# inventory_management/admin.py

from django.contrib import admin
from .models import InventoryItem

def get_column_headings(model_admin):
    return [field.verbose_name.capitalize() for field in model_admin.model._meta.fields]

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name','secondary_name', 'description', 'availability', 'in_use')
    search_fields = ('item_name', 'description')

    def get_column_headings(self, request):
        return get_column_headings(self)
