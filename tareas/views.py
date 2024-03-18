from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Al ejecutarse devuelve un formulario. El segundo cpmprueba si un usuario existe
from django.contrib.auth.models import User # Permite registrar un usuario
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate # Crea las cookies
from .forms import FormTarea
from .models import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
        'form': UserCreationForm,
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registro de usuario
            try:
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                usuario.save() # Lo guarda en la base de datos
                login(request, usuario) # Crea la cookie
                return redirect('tareas')
            except:
                return render(request, 'registrarse.html',{
                    'form': UserCreationForm,
                    'error': 'El nombre de usuario ya existe',
                })
        else:
            return render(request, 'registrarse.html',{
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden',
                })

@login_required            
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas.html', {
        'tareas': tareas,
    })

@login_required            
def tareas_pendientes(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_completada__isnull=True)
    return render(request, 'tareas_pendientes.html', {
        'tareas': tareas,
    })

@login_required 
def tareas_completadas(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_completada__isnull=False).order_by('-fecha_completada')
    return render(request, 'tareas_completadas.html', {
        'tareas': tareas,
    })
    
@login_required 
def cerrarSesion(request):
    logout(request) # Cierra la sesión con la cookie
    return redirect('index')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html',{
        'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'iniciar_sesion.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto/a'
            })
        else:
            login(request, usuario)
            return redirect('tareas')

@login_required 
def crear_tarea(request):   
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {
            'form': FormTarea,
        })
    else:
        try:
            form = FormTarea(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'crear_tarea.html', {
            'form': FormTarea,
            'error': 'Por favor, ingrese un dato válido'
        })
            
@login_required 
def detalle_tarea(request, id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
        form = FormTarea(instance=tarea)
        return render(request, 'detalle_tarea.html', {
            'tarea': tarea,
            'form': form,
        })
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
            form = FormTarea(request.POST,  instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detalle_tarea.html', {'tarea': tarea, 'form': form, 'error': "Error al actualizar tarea"})
        
@login_required 
def tarea_completada(request, id):
    tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
    if request.method == 'POST':
        tarea.fecha_completada = timezone.now()
        tarea.save()
        return redirect(reverse('detalle_tarea', args=[id]))
    
@login_required 
def tarea_incompleta(request, id):
    tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
    if request.method == 'POST':
        tarea.fecha_completada = None
        tarea.save()
        return redirect(reverse('detalle_tarea', args=[id])) 

@login_required 
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')