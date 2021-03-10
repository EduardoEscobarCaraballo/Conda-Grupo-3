from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registroDatos(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'registro\\registro.html', contexts)