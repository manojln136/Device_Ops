from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='dashboard')
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'authentication/login.html')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')


