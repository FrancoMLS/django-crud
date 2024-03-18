from django import forms
from .models import Tarea

class FormTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion','importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese el título'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control mb-3' , 'placeholder': 'Ingrese la descripción', 'required':True}),
        }