from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        modelo = Todo
        campos = "__all__"