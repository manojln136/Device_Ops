#user_management/views.py

from django.shortcuts import render
from .models import User

def user_management_view(request):
    # Fetch all users from the database
    users = User.objects.all()
    return render(request, 'user_management/user_management.html', {'users': users})
