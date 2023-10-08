# RAISE 
# Nos permite generar excepciones propias en un punto específico del programa.

# Ejemplo 01
numero = input("Ingrese un número entero: ")
numero = int(numero)
print(numero)
division = 1000 / 0

if numero == 15:
    raise ValueError("No se admite el valor de 15")
elif numero == 30:
    raise ValueError("No se permite el valor de 30")

# Ejemplo 02
class Persona:
    def __init__(self, usuario, password, permisos):
        self.usuario = usuario
        self.password = password
        self.permisos = permisos


def estado_permiso(objeto):
    if objeto.permisos: 
        print("Usted tiene acceso.")
    else:
        raise Exception("Usted no tiene acceso.")
    

persona01 = Persona("Luis", "123456", True)
persona02 = Persona("Andrea", "123abc", False)

estado_permiso(persona01)
estado_permiso(persona02)