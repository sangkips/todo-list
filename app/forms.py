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
    
