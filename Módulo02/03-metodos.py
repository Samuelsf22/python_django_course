# Eliminar objetos __del__ (Eliminar un objeto específico)
""" 
class Zapatilla:
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año
        print(f"Tienes una zapatilla de marca: {self.marca}")
        print(f"De color: {self.color} del año: {self.año}")

    def __del__(self):
        print("Se ha eliminado el objeto derivado de la clase Zapatilla")


mizapatilla = Zapatilla("Nike", "Blanco", 2023)
print("**************")
print(mizapatilla)
print("**************")
del(mizapatilla)
"""

# Método STR
# mostrar una parte o el total del objeto)
""" 
class Auto:
    def __init__(self, marca, color, kilometraje, año):
        self.marca = marca
        self.color = color
        self.kilometraje = kilometraje
        self.año = año
        print(f"Se ha comprado el auto {self.marca} del año {self.año}")

    def __str__(self):
        return f"El auto es un {self.marca}, de color {self.color}, tiene {self.kilometraje} Km, siendo del año {self.año}"

miauto = Auto("Ferrari", "Rojo", 159, 2022)
print(miauto)
"""
# Encapsulamiento
# pi = 3.1425
# nos sirve para ciertos atributos y caracteristicas no sean modificables desde el exterior.

class Moto:
    def __init__(self):
        self.marca = "HONDA"
        self.color = "blanco"
        self.__ruedas = 2
        self.enMarcha = False

    def estado(self, estadoActual):
        self.enMarcha = estadoActual
        if self.enMarcha:
            return "La moto está encendida"
        else:
            return "La moto está apagada"
        
    def __str__(self):
        return f"La moto es un {self.marca}, de color {self.color}, de {self.__ruedas} ruedas"


mimoto1 = Moto()
print(mimoto1.estado(False))

print("***********Modificación externa***********")
mimoto2 = Moto()
mimoto2.__ruedas = 15
print(mimoto2.estado(False))
print(mimoto2)

