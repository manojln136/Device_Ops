# inventory_management/models.py

from django.db import models

class InventoryItem(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    item_name = models.CharField(max_length=100)
    secondary_name = models.CharField(max_length=100, blank=True, null=True)  # New column
    description = models.TextField()
    availability = models.IntegerField(default=0)
    in_use = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
