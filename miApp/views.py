from django.shortcuts import render
from .models import Todo

# Create your views here.

def index(request):
    lista_items = Todo.objects.order_by("-date")
    if request.METHOD == "POST":
        form = Todo
    
    
    return render(request, 'index.html')