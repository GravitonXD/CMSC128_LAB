from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'text-input', 'title': 'Username'}),
        }
