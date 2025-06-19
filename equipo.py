# Este archivo contiene las definiciones de nuestras clases.
# Es buena práctica tener las importaciones necesarias para la clase aquí mismo.
from datetime import datetime

class Equipo:
    """
    Representa un equipo electrónico ingresado para reparación.
    """
    def __init__(self, id, modelo, problema, precio=None, pago=None, contraseña=None):
        self.id = id
        self.modelo = modelo
        self.problema = problema
        self.precio = precio
        self.pago = pago
        self.contraseña = contraseña
        self.fecha_ingreso = datetime.now()
        self.estado = "Ingresado"

    def __str__(self):
        fecha_f = self.fecha_ingreso.strftime("%d/%m/%Y %H:%M")
        info = (
            f"--- Ficha del Equipo ID: {self.id} ---\n"
            f"  Modelo: {self.modelo}\n"
            f"  Problema: {self.problema}\n"
            f"  Estado: {self.estado}\n"
            f"  Fecha de Ingreso: {fecha_f}\n"
        )
        if self.precio is not None:
            info += f"  Precio Reparación: ${self.precio:.2f}\n"
        if self.pago is not None:
            info += f"  Monto Pagado: ${self.pago:.2f}\n"
        if self.contraseña:
            info += f"  Contraseña: {self.contraseña}\n"
        info += "------------------------------"
        return info

    def asignar_precio(self, monto):
        if monto >= 0:
            self.precio = float(monto)
            self.actualizar_estado("Diagnosticado")
            print(f"Precio ${monto:.2f} asignado al equipo ID {self.id}.")
        else:
            print("Error: El precio no puede ser negativo.")

    def registrar_pago(self, monto):
        if monto > 0:
            if self.pago is None:
                self.pago = 0.0
            self.pago += float(monto)
            print(f"Pago de ${monto:.2f} registrado para el equipo ID {self.id}. Total pagado: ${self.pago:.2f}.")
        else:
            print("Error: El monto a pagar debe ser positivo.")

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado del equipo ID {self.id} ha sido actualizado a: '{nuevo_estado}'.")

# Nota: Este archivo NO tiene el código del ABM ni la sección if __name__ == "__main__".
# Solo contiene la "plantilla" de la clase.