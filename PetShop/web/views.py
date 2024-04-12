from django.shortcuts import render


# Create your views here.

def index (request):
    return render (request,'index.html')

def gato (request):
    return render (request,'gato.html')

def perro (request):
    return render (request,'perro.html')

def carro (request):
    return render (request,'carro.html')

def iniciar (request):
    return render (request,'iniciarsesion.html')

def perfil (request):
    return render (request,'pefil.html')

def recupera (request):
    return render (request,'recuperapass.html')

def user (request):
    return render (request,'user_reg.html')
