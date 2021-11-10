from typing import Optional
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'placeholder':'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'input', 'title': 'FirstName', 'placeholder': 'First Name'}),
            'last_name': widgets.TextInput(attrs={'class': 'input', 'title': 'LastName', 'placeholder': 'Last Name'}),
            'username': widgets.TextInput(attrs={'class': 'input', 'title': 'Username', 'placeholder': 'Username'}),
            'email': widgets.EmailInput(attrs={'class': 'input', 'title': 'Email', 'placeholder': 'Email'}),
        }
