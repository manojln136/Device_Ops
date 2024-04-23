from django.shortcuts import render
from .models import InventoryItem

def inventory_view(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'inventory_management/inventory_management.html', {'inventory_items': inventory_items})
