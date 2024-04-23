from django.shortcuts import render

def reservation_management_view(request):
    return render(request, 'reserve_management/reserve_mangement.html')
