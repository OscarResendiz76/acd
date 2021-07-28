"""arteycultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


from arteycultura.views import ingresar, inicio, enviarCorreo, registrarUsuario,salir
from registro.views import registro
from arte.views import ListaActividades, agregar as agregarArte, inicio as inArte
from deportes.views import agregar, inicio as inDeporte 
from deportes.views import ListaDeportes 
from registro.views import ListaRegistro




urlpatterns = [
    path('admin/', admin.site.urls),
    #url("registro",registro),
    url(r"^$",inicio),
    url(r"arte$",ListaActividades.as_view()),
    url(r"deportes$",ListaDeportes.as_view()),
    url(r"registro$",ListaRegistro.as_view()),
    url(r"^deportes$",inDeporte),
    url(r"^arte$",inArte),
    url(r"^arte/add$", agregarArte),
    url(r"^deportes/add$", agregar),
    url(r"^correo$",enviarCorreo),
    url(r"^login$",ingresar),
    url(r"^logout$",salir),
    url(r"^registro/add$",registrarUsuario),
]
