from django.shortcuts import render
from custom_user import settings

# Create your views here.

def home_view(request):
    data = getattr(settings, 'AUTH_USER_MODEL', None)
    return render (request, 'home.html', {'data': data})
