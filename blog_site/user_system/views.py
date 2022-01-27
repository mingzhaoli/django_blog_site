from django.shortcuts import render, get_object_or_404

from user_system.forms import SignUpForm, LoginForm

from django.contrib.auth.models import User

# Create your views here.

def user_profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_system/user_profile.html', {'user': user})

def user_login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print ("Logged In")
    
    context = {
        'form': form
    }
    return render(request, 'user_system/user_login.html', context)

def user_creation_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, 'user_system/user_creation.html', context)