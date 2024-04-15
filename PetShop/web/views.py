from django.shortcuts import render
from .models import Usuario

# Create your views here.

def index (request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        print("Datos del form", username, password)
        usuarioBD = Usuario.objects.filter(username=username).first()
        if usuarioBD is not None:
            if usuarioBD.password == password:
                if usuarioBD.perfil.perfil == "Administrador":
                    print("Home administrador")
                    return render(request, 'web/productos.html')
                if usuarioBD.perfil.perfil == "Usuario":
                    print("Home usuario")
                    return render(request, 'web/productos.html')
                else:
                    print("No se encontro perfil")
                    return render(request,'web/index.html')
            else:
                print("Password incorrecta")
                return render(request,'web/index.html')
        else:
            print("Usuario no existe")
            return render(request,'web/index.html')
    else:
        return render(request,'web/index.html')

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
