from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=150),
    detalles = models.CharField(max_length=555),
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
## Creacion y eliminacion de una tarea
## Al hacer click en un boton para completar, el estado de la tarea se cambia
## Conexion a una base de datos externa -> Oracle
## Uso de variables de entorno con django.environ
## gitignore
## subir a github

    
    
