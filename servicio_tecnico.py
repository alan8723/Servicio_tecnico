from user import Usuario
from equipo import Equipo

# --- Base de Datos en Memoria ---
# En un programa real, esto estaría en una base de datos, pero para probar,
# usaremos listas que guardarán nuestros objetos.
lista_usuarios = []
siguiente_id_equipo = 1 # El ID de Usuario se autogestiona, pero el de Equipo no.

def registrar_nuevo_ingreso():
    """
    Función que maneja el formulario en consola para registrar 
    un nuevo usuario y su equipo.
    """
    global siguiente_id_equipo # Avisamos que usaremos la variable global para el ID

    print("\n--- [ FORMULARIO DE NUEVO INGRESO ] ---")
    
    # 1. Solicitar datos del Cliente (Usuario)
    print("\n--- Datos del Cliente ---")
    nombre_cliente = input("Nombre completo: ")
    dni_cliente = input("DNI: ")
    numero_cliente = input("Número de teléfono/contacto (opcional): ")

    # 2. Solicitar datos del Equipo
    print("\n--- Datos del Equipo ---")
    modelo_equipo = input("Modelo del equipo (Ej: iPhone 13, Notebook HP Pavilion): ")
    problema_equipo = input("Descripción del problema: ")
    pass_equipo = input("Contraseña del equipo (opcional, para pruebas): ")

    # 3. Crear los objetos
    print("\nProcesando información...")
    
    # Creamos primero el objeto Equipo
    nuevo_equipo = Equipo(
        id=siguiente_id_equipo,
        modelo=modelo_equipo,
        problema=problema_equipo,
        contraseña=pass_equipo
    )
    siguiente_id_equipo += 1 # Incrementamos el ID para el próximo equipo

    # Creamos el objeto Usuario, pasándole una lista que contiene el equipo recién creado
    nuevo_usuario = Usuario(
        nombre=nombre_cliente,
        dni=dni_cliente,
        numero=numero_cliente,
        equipo_de_usuario=[nuevo_equipo] # Pasamos el equipo dentro de una lista
    )

    # 4. Guardar en nuestra "base de datos"
    lista_usuarios.append(nuevo_usuario)

    # 5. Confirmación al usuario
    print("\n¡REGISTRO EXITOSO!")
    print("--------------------")
    print("Se ha creado el siguiente cliente:")
    print(repr(nuevo_usuario)) # Usamos repr para ver la info del objeto usuario
    print("\nCon el siguiente equipo asociado:")
    print(str(nuevo_equipo)) # Usamos str para ver la ficha del equipo

def mostrar_todos_los_usuarios():
    """Muestra un resumen de todos los usuarios y sus equipos."""
    print("\n--- [ LISTA DE TODOS LOS CLIENTES ] ---")
    if not lista_usuarios:
        print("No hay clientes registrados.")
        return
        
    for user in lista_usuarios:
        print(f"\n========================================")
        print(f"CLIENTE ID: {user.id} | Nombre: {user.nombre} | DNI: {user.dni}")
        print("----------------------------------------")
        if not user.equipos:
            print(" >> No tiene equipos registrados.")
        else:
            print(" >> Equipos Registrados:")
            for eq in user.equipos:
                print(f"   - ID Equipo: {eq.id} | Modelo: {eq.modelo} | Estado: {eq.estado}")
    print(f"========================================")

# --- Menú Principal del Programa ---
if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión del Taller")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Nuevo Cliente y Equipo")
        print("2. Ver todos los Clientes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_nuevo_ingreso()
        elif opcion == '2':
            mostrar_todos_los_usuarios()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")