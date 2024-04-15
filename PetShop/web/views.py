from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.

def index (request):
    if request.method == 'POST':
        username_login = request.POST.get('user_login')
        password = request.POST.get('password')
        print("Datos del form", username_login, password)
        usuarioBD = Usuario.objects.filter(username=username_login).first()
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

def user(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        run = request.POST.get('run')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fechanac = request.POST.get('fechanac')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Datos", run, nombres, apellidos, username, password, email, fechanac, ciudad, direccion)
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")

        # Guardar los datos en la base de datos
        usuario = Usuario(
            run=run,
            nombres=nombres,
            apellidos=apellidos,
            username=username,
            password=password,
            email=email,
            fechanac=fechanac,
            ciudad_id=ciudad,
            direccion=direccion,
        )
        usuario.save()

        return render(request, 'web/index.html')
    else:
        return render(request,'web/user_reg.html')

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

#def user (request):
#    return render (request,'web/user_reg.html')

def base (request):
    return render (request, 'web/base.html')
