from django.shortcuts import render

# Create your views here.


def configuracionDatos(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'configuracion\configuracion.html', contexts)
    