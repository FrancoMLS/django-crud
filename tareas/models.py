from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True) # Con el blank=True si no pasan nada al campo, por defecto el campo estará vacío
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Con esto se agrega por defecto la fecha si el campo no se completa
    fecha_completada = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.titulo} - creada por {self.usuario}' # Regresa el nombre del titulo en el localhost/admin