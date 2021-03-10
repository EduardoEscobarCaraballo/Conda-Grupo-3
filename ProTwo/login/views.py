from django.shortcuts import render

# Create your views here.
def loginDatos(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'login\\login.html', contexts)