from django.shortcuts import render

# Create your views here.

def informacionDatos(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'descripcion': 'Texto de prueba 4'
    }
    return render(request, 'informacion\\informacion.html', contexts)