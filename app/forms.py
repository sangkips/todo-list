from django.contrib.auth.models import User
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput)

