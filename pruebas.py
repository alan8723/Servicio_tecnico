import json
import os

NOMBRE_ARCHIVO = "servicio_tecnico.json"

def leerJson():
# --- Paso 2: Leer la lista actual de datos ---
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        # Cargamos el contenido del archivo en una lista de Python
        base_de_datos = json.load(archivo)
        return base_de_datos

def escribirJson(data):
    #Asegurarse de que el archivo exista y sea una lista válida ---
    # Si el archivo no existe o está vacío, lo creamos con una lista vacía [].
    if not os.path.exists(NOMBRE_ARCHIVO) or os.path.getsize(NOMBRE_ARCHIVO) == 0:
        with open(NOMBRE_ARCHIVO, "w") as archivo:
            json.dump([], archivo) # Escribe una lista vacía
        #Escribir la lista completa y actualizada de vuelta en el archivo ---
    else:
        nueva_bd = json.dump(leerJson())
        nueva_bd.append(json(data))
        with open(NOMBRE_ARCHIVO, "w") as archivo:
            # Escribimos toda la lista modificada
            json.dump(nueva_bd, archivo, indent=4)
            print(f"\n¡Nuevo ingreso guardado con éxito en '{NOMBRE_ARCHIVO}'!")

persona1={
    "nombre": "carlos",
    "equipo": "moto g14",
    "numero": "2211223344"
}

persona2={
    "nombre": "pedro",
    "equipo": "moto g6",
    "numero": "1122334455"
}

persona3={
    "nombre": "valeria",
    "equipo": "A15",
    "numero": "7755336699"
}

escribirJson(persona1)
print("\nDatos después de añadir el nuevo ingreso:")
print(leerJson())














