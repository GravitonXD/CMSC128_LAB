import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
        max_length=20,
        required=True)
    
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
        max_length=15,
        required=True)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
        max_length=10,
        required=True)

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
        max_length=30,
        required=True)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
        max_length=15,
        required=True)

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirm Password'}),
        max_length=15,
        required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    email = forms.EmailField(
        label='E-mail',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'E-mail'}),
        required=True)
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'placeholder':'Password'}),
        required=True,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'placeholder':'Confirm Password'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    # Check if username is already taken
    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is taken")
        return username
    
    # Check if email is already taken, and if it is not check if it is a valid email
    # It is valid if it ends with a .com or .edu.ph
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already taken")
        if not email.endswith('.com') and not email.endswith('.edu.ph') and not '@' in email:
            raise forms.ValidationError("Invalid email")
        return email

    # Check if password is atleast 8 characters long, has at least one uppercase letter, one lowercase letter, one symbol, and one number
    def clean_password1(self, *args, **kwargs):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("Password must be atleast 8 characters long")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must have atleast one uppercase letter")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("Password must have atleast one lowercase letter")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must have atleast one number")
        if not re.search(r'[!@#$%^&*()]', password):
            raise forms.ValidationError("Password must have atleast one symbol")
        return password

        
    # Check if password and confirm password match
    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
