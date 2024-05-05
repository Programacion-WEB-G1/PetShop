function Validar (){
    verificarContrasena();
    validarEdad();

}
function verificarContrasena() {
    var pass1 = document.getElementById("inputPassword6").value;
    var pass2 = document.getElementById("inputPassword7").value;
    var tieneMayuscula = /[A-Z]/.test(pass1);
    var tieneNumero = /[0-9]/.test(pass1);
    if (tieneMayuscula && tieneNumero) {
    } else {
        alert(
            "La contraseña debe contener al menos una mayúscula y un número."
        );
        return;
    }
    if (pass1 === pass2) {
    } else {
        alert("Las contraseñas deben ser iguales");
    }
}

  function validarEdad() {
    var fechaInput = document.getElementById("validationDefault05").value;
    var fechaNacimiento = new Date(fechaInput);
    var hoy = new Date();
    var edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    var mes = hoy.getMonth() - fechaNacimiento.getMonth();

    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
      edad--;
    }

    if (edad < 18) {
      alert("Debes ser mayor de 18 años para acceder.");
      return false;
    }

    return true;
}

function agregarAlCarrito(productId) {
    fetch('/agregar-al-carrito/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ producto_id: productId })
    })
    .then(response => {
        if (response.ok) {
            alert('Producto agregado al carrito correctamente');
            // Aquí podrías realizar alguna acción adicional, como actualizar la vista del carrito
        } else {
            alert('Error al agregar el producto al carrito');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al agregar el producto al carrito');
    });
}


(function() {
    document.getElementById('btn-editar').addEventListener('click', function() {
        // Mostrar el formulario de edición
        document.getElementById('form-edicion').style.display = 'flex';
    });
    
    document.addEventListener('DOMContentLoaded', function() {
        // Obtener y mostrar los elementos del carrito al cargar la página
        fetch('/obtener-carrito/')
        .then(response => response.json())
        .then(data => {
            const cartItems = document.getElementById('cart-items');
            cartItems.innerHTML = ''; // Limpiar los elementos del carrito existentes
    
            // Iterar sobre los elementos del carrito recibidos del servidor
            data.cart.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.textContent = `Producto: ${item.nombre}, Precio: ${item.precio}`;
                cartItems.appendChild(itemElement);
            });
    
            // Agregar event listener para el botón "Agregar al Carrito"
            document.querySelectorAll('.add-to-cart').forEach(button => {
                button.addEventListener('click', function() {
                    const productId = this.dataset.productId; // Obtener el ID del producto
                    agregarAlCarrito(productId); // Llamar a la función para agregar al carrito
                });
            });
        })
        .catch(error => console.error('Error:', error));
    
        // Resto del código...
    });
    });