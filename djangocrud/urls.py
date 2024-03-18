"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('tareas/', views.tareas, name='tareas'),
    path('logout/', views.cerrarSesion, name='cerrar_sesion'),
    path('iniciar-sesion/', views.iniciarSesion, name='iniciar_sesion'),
    path('tareas/crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/', views.detalle_tarea, name="detalle_tarea"),
    path('tareas/<int:id>/completada', views.tarea_completada, name="tarea_completada"),
    path('tareas/<int:id>/eliminar', views.eliminar_tarea, name="eliminar_tarea"),
    path('tareas_completadas/', views.tareas_completadas, name='tareas_completadas'),
    path('tareas/<int:id>/incompleta', views.tarea_incompleta, name='tarea_incompleta'),
    path('tareas_pendientes/', views.tareas_pendientes, name='tareas_pendientes'),
    
    
    
]
