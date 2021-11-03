from django.shortcuts import render
from django.http import HttpResponse


def dashBoard(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'sign_up.html')

def login(request):
    return render(request, 'login.html')
