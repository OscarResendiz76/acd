from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from deportes.formulario import FormularioDeportes
from .models import Deportes
from django.views import generic

def inicio(request):
    return HttpResponse("<a href='deportes/add'>Agregar</a>")

# Create your views here.
def agregar(request):
    f = FormularioDeportes()
    if request.method =="POST":
        f= FormularioDeportes(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/") 

    return render(request,"deportes.html",{"form":f})

class ListaDeportes(generic.ListView):
    model = Deportes 
    context_object_name= "actividadesdeporte"
    template_name = "deporte.html"