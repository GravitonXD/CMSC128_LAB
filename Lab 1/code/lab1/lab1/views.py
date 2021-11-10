from typing import ContextManager
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from templates.createUser import CreateUserForm
from django.contrib import messages

# render index.html when at /home
def home(request):
    return render(request, 'index.html')

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

def signUp(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, form.errors)

    context = {'form': form}
    return render(request, 'sign_up.html', context)