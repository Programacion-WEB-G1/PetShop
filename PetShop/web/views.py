from django.shortcuts import render


# Create your views here.

def index (request):
    return render (request,'web/index.html')

def gato (request):
    return render (request,'web/gato.html')

def perro (request):
    return render (request,'web/perro.html')

def carro (request):
    return render (request,'web/carro.html')

def producto (request):
    return render (request,'web/productos.html')

def perfil (request):
    return render (request,'web/miperfil.html')

def recupera (request):
    return render (request,'web/recuperapass.html')

def user (request):
    return render (request,'web/user_reg.html')

def base (request):
    return render (request, 'web/base.html')
