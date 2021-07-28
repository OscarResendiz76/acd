
from django.shortcuts import redirect, render
from .formulario import FormularioPersona
from .models import Persona
from django.views import generic

# Create your views here.
def registro(request):
    formulario = FormularioPersona()
    if request.method == "POST":
        formulario=FormularioPersona(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre=request.POST["nombre"]
            apellido=request.POST["apellidos"]
            correo=request.POST["correo"]
            sexo=request.POST["sexo"]
            print(nombre)
            return redirect("/?",nombre)
    return render(request,"registro.html",{"form":formulario})

class ListaRegistro(generic.ListView):
    model = Persona 
    context_object_name= "listaregistro"
    template_name = "registro.html"