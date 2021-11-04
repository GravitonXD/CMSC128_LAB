from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'sign_up.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def planner(request):
    return render(request, 'planner.html')

def profile(request):
    return render(request, 'profile.html')