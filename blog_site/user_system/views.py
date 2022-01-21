from django.shortcuts import render, get_object_or_404

from .models import User

# Create your views here.

def user_profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_system/user_profile.html', {'user': user})

def user_login_view(request):
    return render(request, 'user_system/user_login.html', {})