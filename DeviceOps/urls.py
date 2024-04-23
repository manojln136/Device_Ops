"""
URL configuration for DeviceOps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication import views
from authentication.views import login_view, logout_view
from inventory_management.views import inventory_view  
from user_management.views import user_management_view 
from reserve_management.views import reservation_management_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='default_login'),
    path('', logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    path('inventory/', inventory_view, name='inventory_management'),  # Corrected name
    path('user/', user_management_view, name='user_management'),  # Corrected name
    path('reservation/', reservation_management_view, name='reservation_management'),
]  # Added missing closing parenthesis


