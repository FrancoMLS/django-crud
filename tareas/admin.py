from django.contrib import admin
from .models import Tarea

class AdminTareas(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', )

# Register your models here.
admin.site.register(Tarea, AdminTareas) # Hace aparecer la tabla de Tarea en el localhost/admin