# ----------------------------------------------------------------
# SIMULACIÓN DE BASE DE DATOS EN MEMORIA
# ----------------------------------------------------------------
# Usamos una lista de diccionarios para simular la base de datos.
# Usamos un contador para generar IDs únicos y autoincrementales.

# Es importante importar la clase Equipo para poder usarla
from equipo import Equipo

class Usuario:
    """
    Representa a un único usuario en el sistema.
    El ID se autoincrementa y es gestionado por la propia clase.
    """
    _id_counter = 1

    def __init__(self, nombre, dni, equipo_de_usuario, numero=None):
        """
        Constructor para un nuevo usuario.
        """
        self.id = Usuario._id_counter
        self.nombre = nombre
        self.dni = dni
        self.numero = numero
        
        # CORRECCIÓN 1: Comparamos con la clase Equipo
        # Se asegura de que en la lista inicial solo haya objetos de tipo Equipo.
        if equipo_de_usuario:
             self.equipos = [c for c in equipo_de_usuario if isinstance(c, Equipo)]
        else:
            self.equipos = []
        
        Usuario._id_counter += 1

    def __repr__(self):
        """
        Representación oficial del objeto.
        """
        return f"Usuario(id={self.id}, nombre='{self.nombre}', dni='{self.dni}', numero='{self.numero}')"

    def actualizar(self, nuevo_nombre, nuevo_numero):
        """
        Actualiza los datos del usuario.
        """
        self.nombre = nuevo_nombre
        self.numero = nuevo_numero

    def new_equipo(self, nuevo_equipo):
        if isinstance(nuevo_equipo, Equipo):
            self.equipos.append(nuevo_equipo)
            print(f"El equipo {nuevo_equipo.modelo} ha sido añadido al usuario {self.nombre}.")
        else:
            print("Error: solo se puede añadir objetos de la clase Equipo al usuario.")
            
    def quit_equipo(self, id_equipo):
        """
        Busca un equipo por su ID y lo elimina de la lista del usuario.
        """
        equipo_delet = None
        for equipo in self.equipos:
            if equipo.id == id_equipo:
                equipo_delet = equipo
                # CORRECCIÓN 2: El break va DENTRO del if.
                break 

        if equipo_delet:
            self.equipos.remove(equipo_delet)
            print(f"El equipo con ID {equipo_delet.id} ha sido eliminado del usuario {self.nombre}.")
        else:
            print(f"No se encontró ningún equipo con el ID {id_equipo} para este usuario.")
