from django import forms

from .models import  Deportes 

class FormularioDeportes(forms.ModelForm):
    
    class Meta:
    
        model = Deportes

        fields=["nombre","descripcion"]