from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout,login, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Usuario, Categoria, Producto
from django.contrib.auth.models import User # angel modifico a ca
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = request.POST.get('user_login')
        pass_login = request.POST.get('pass_login')
        print("Datos del formulario", user_login, pass_login)
        try:
            usuarioBD = Usuario.objects.get(username=user_login)
            if usuarioBD.perfil.perfil == "Administrador" or usuarioBD.perfil.perfil == "Usuario":
                print("Inicio de sesión exitoso")
                user = authenticate(username=user_login, password=pass_login)
                user.data = usuarioBD
                if user is not None:
                    login(request, user)
                    return redirect('productos')  # Redirecciona a la página de productos
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
        user = User.objects.create_user(username, email, password)
        user = user.save()
        return redirect('index')  # Redirecciona a la página de inicio
    else:
        return render(request, 'web/user_reg.html')
    
def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Redirecciona al inicio u otra página después de cerrar sesión

def productos_perro(request):
    categoria_perro = Categoria.objects.get(nombre_categoria="Comida Perro")
    productos_perro = Producto.objects.filter(categoria=categoria_perro)
    return render(request, 'web/perro.html', {'productos_perro': productos_perro})

def productos_gato(request):
    categoria_gato = Categoria.objects.get(nombre_categoria="Comida Gato")
    productos_gato = Producto.objects.filter(categoria=categoria_gato)
    return render(request, 'web/gato.html', {'productos_gato': productos_gato})

def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        return JsonResponse({'mensaje': f'Producto {producto_id} agregado al carrito correctamente'})
    else:
        return JsonResponse({'error': 'La solicitud debe ser de tipo POST'})

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

def miperfil(request):
  
    usuarioBD = Usuario.objects.get(username=request.user)

    datos = {
        'name':usuarioBD.nombres,
        'address':usuarioBD.direccion,
        'email':usuarioBD.email,
        'username': request.user,
        'birthdate': usuarioBD.fechanac 
    }
    return render(request,'web/miperfil.html',datos)

def api_pet(request):
    return render (request,'web/api_pet.html')

@csrf_exempt
def reset_password(request):

    if request.method == 'POST':
        # Obtener el nombre de usuario y la nueva contraseña del formulario
        username = request.POST.get('username')
        new_password = request.POST.get('password')
        
        # Restablecer la contraseña del usuario en la base de datos
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            # Redirigir a una página de confirmación o iniciar sesión nuevamente
            return render(request, 'web/password_reset_success.html')
        except User.DoesNotExist:
            # Manejar el caso en el que no se encuentre el usuario
            print("El usuario no existe.")
            return render(request, 'web/password_reset_error.html')
        except Exception as e:
            # Capturar cualquier otro error y mostrarlo por pantalla
            print("Error:", e)
            return render(request, 'web/password_reset_error.html')
    else:
        # Si no es una solicitud POST, renderizar el formulario de restablecimiento de contraseña
        return render(request, 'web/reset_password.html')

def api_pet2(request):
    return render (request,'web/api_pet2.html')

