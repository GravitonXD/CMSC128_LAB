from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from templates import createUser

# render index.html when at /home
def home(request):
    return render(request, 'index.html')

# render signup.html when at /signup
def signUp(request):
    return render(request, 'sign_up.html')

# render login.html when at /login
def login(request):
    return render(request, 'login.html')

# render about.html when at /about
def about(request):
    return render(request, 'about.html')

# render contact.html when at /contact
def contact(request):
    return render(request, 'contact.html')

# render planner.html when at /planner
def planner(request):
    return render(request, 'planner.html')

# render profile.html when at /profile
def profile(request):
    return render(request, 'profile.html')

    
