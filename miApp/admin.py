from django.contrib import admin
from .models import Todo
from .forms import TodoForm

# Register your models here.
admin.site.register(Todo)