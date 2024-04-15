from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Usuario

# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = request.POST.get('user_login')
        pass_login = request.POST.get('pass_login')
        print("Datos del formulario", user_login, pass_login)
        try:
            usuarioBD = Usuario.objects.get(username=user_login)
            if usuarioBD.password == pass_login:
                if usuarioBD.perfil.perfil == "Administrador" or usuarioBD.perfil.perfil == "Usuario":
                    print("Inicio de sesión exitoso")
                    return redirect('productos')  # Redirecciona a la página de productos
                else:
                    print("No se encontró un perfil adecuado")
                    messages.error(request, "Perfil incorrecto")
                    return render(request, 'web/index.html')
            else:
                print("Contraseña incorrecta")
                messages.error(request, "Contraseña incorrecta")
                return render(request, 'web/index.html')
        except Usuario.DoesNotExist:
            print("Usuario no encontrado")
            messages.error(request, "Usuario no encontrado")
            return render(request, 'web/index.html')
    else:
        return render(request, 'web/index.html')

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

        return redirect('index')  # Redirecciona a la página de inicio
    else:
        return render(request, 'web/user_reg.html')
    
def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Redirecciona al inicio u otra página después de cerrar sesión

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

def base (request):
    return render (request, 'web/base.html')
