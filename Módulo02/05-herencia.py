# HERENCIA
# Se tiene una clase (clase padre / clase madre) - SUPERCLASE, CLASE PRINCIPAL
# permitir heredar: Atributos, métodos a otra clases llamadas, clases hijas(os) CLASE SECUNDARIA. __spec__
#                 CLASE 01

#                 CLASE 02

#     CLASE 03    CLASE 04    CLASE 05

""" 
Persona :
    Atributos:  Apellidos
                Nombres
                DNI

    Metodos :   Caminar
                Hablar
                Cantar
                Bailar

HIJO                ESPOSO(a)

Apellidos           Apellidos
Nombres             NombresA
DNI                 DNI

hacer tareas        apoyar en casa
pedir permiso       trabajar
cantaria            viajar
"""
""" 
class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    def mostrarDatos(self):
        print(f"Hola, {self.nombre + self.apellido}")
        print(f"Eres {self.sexo} de {self.edad} años")

# miPersona = Persona("Calors", 29, "Espinoza", "Varón")
# miPersona.mostrarDatos()
print("******************************")

class Colaborador(Persona):
    def datosColaborador(self, sueldo, vacaciones):
        self.sueldo = sueldo * 1.1
        self.vacaciones = vacaciones + 3
        print(f"el sueldo recibido es : {self.sueldo:.2f}")
        print(f"Sus vacaciones son de: {self.vacaciones} días")

colaborador_1 = Colaborador("Jose", 25, "Ortega", "Varón")
colaborador_1.mostrarDatos()
colaborador_1.datosColaborador(2800, 15)
"""

# PROBLEMA 01
# Elaborar una LI, en la cual se tenga una clase Persona, con un método inicializador que permita capturar el nombre y la edad
# así como otro método que permita mostrar en el prompt los datos de la Persona
# Luego crear una clase "Empleado" que herede de la clase "Persona"
# la clase empleado debe contar con su propio atributo de sueldo, y luego mediante un método imprimir sus datos,
# finalmente otro método "impuesto" que permita saber cuanto pagaría en caso  los 1500
""" 
class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad:"))

    def imprimir(self):
        print(f"Hola {self.nombre}, tu tienes {self.edad} años")

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese su sueldo actual: "))

    def imprimir(self):
        super().imprimir()
        print(f"Su sueldo actual es: {self.sueldo}")
              
    def impuesto(self):
        if self.sueldo > 1500:
            self.impuesto = self.sueldo * 0.08
            print(f"Por favor pagar los impuestos de: {self.sueldo}")
        else:
            print("No te corresponde pagar impuestos.")
    

empleado = Empleado()
empleado.imprimir()
empleado.impuesto()
"""


# Problema 02
# Elaborar una LI, en Ia cual contenga Ia superclase "Persona" con un inicializador que cuente con los
# atributos de apellidos nombres, dni y edad. (se solicita estos datos para ingresarlos por teclado)
# Luego crear una clase trabajador, que herede de Ia superclase, dicha clase cuente con un par de atributos de
# sueldo y dias de vacaciones.
# Ia clase trabajador debera contar con metodos que permitan mostrar los datos, cuanto es el descuento por AFP (13%),
# y los dias de vacaciones que tendra. (Tanto los datos como dias de vacaciones deberos ser incluir en un solo metodo)
""" 
class Persona:
    def __init__(self):
        self.apellidos = input("Ingrese sus apellidos: ")
        self.nombres = input("Ingrese sus nombres: ")
        self.dni = input("Ingrese sus dni: ")
        self.edad = input("Ingrese sus edad: ")
    
    def imprimirDatos(self):
        print("Los datos ingresados son:\n")
        print(f"{self.apellidos} - {self.nombres} - {self.dni} - {self.edad}")

class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese su sueldo actual:"))
        self.vacaciones = int(input("Ingrese cuantos días de vaciones tendrá: "))

    def datos_tranbajador(self):
        super().imprimirDatos()
        print(f"Su sueldo actual es de {self.sueldo}")
        print(f"Los días de vaciones asignados son : {self.vacaciones} días")

    def descuentoAFP(self):
        self.descuento = self.sueldo * 0.13
        print(f"El descuento aplicado por concepto de AFP es: {self.descuento:.2f}")

trabajador = Trabajador()
trabajador.datos_tranbajador()
trabajador.descuentoAFP()
"""

# HERENCIA MULTIPLE
# Es wn la cual una clase puede heredar de una o más clases padres.

class OperacionesElementales:
    def suma(self, num1, num2):
        self.suma = num1 + num2
        print(f"La suma es : {self.suma}")

    def resta(self, num1, num2):
        self.resta = num1 - num2
        print(f"La resta es : {self.resta}")
    
class OperacionesIntermedias:
    def multiplicacion(self, num1, num2):
        self.multiplicacion = num1 * num2
        print(f"La multiplicacion es : {self.multiplicacion}")

    def division(self, num1, num2):
        self.division = num1 / num2
        print(f"La division es : {self.division}")

class Operacion(OperacionesElementales, OperacionesIntermedias):
    def saludoBienvenida(self):
        print("Aprende oporeciones elementales e intermedias")

operacion1 = Operacion()
operacion1.saludoBienvenida()
operacion1.suma(25,25)
operacion1.multiplicacion(14,15)
operacion1.resta(156,1561)
operacion1.division(14,5)
