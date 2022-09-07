from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from app.models import Todo
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product description'}),
        }


class CreateFormUser(UserCreationForm):
    models = User
    fields = '__all__'
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}),
    }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput)

