from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chatPrivadoDatos(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'usuario2_var': 'NombreUsuario2',
        'mensaje1': 'Hola bb',
        'mensaje2': 'Holaaaaaaa'
    }
    return render(request, 'chatPrivado\chatPrivado.html', contexts)