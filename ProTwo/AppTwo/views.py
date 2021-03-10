from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<em>Primera vista</em>')


def index2(request):
    contexts = {
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'likes': '500 me gusta',
        'caption': 'Cogito ergo sum'
    }
    return render(request, 'AppTwo\\index.html', contexts)


