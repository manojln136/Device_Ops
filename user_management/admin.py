#user_management/admin.py

from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'department', 'email_id')
    search_fields = ('employee_id', 'employee_name', 'department', 'email_id')
    ordering = ('employee_id',)

admin.site.register(User, UserAdmin)
