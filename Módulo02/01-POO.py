""" 
PROGRAMACIÓN ORIENTADAD A OBJETOS

Vamos a trabajar con clases(objetos) y la creación de objetos(definir objetos o instanciar objetos)

Objeto, clase, atributo, metodo.

OBJETO: Es todo aquello que se puede abstraer de la vida real, en la cual tiene sus propias caracteristicas
(sus daros, sus informacion, su porgramación, realizacion de acciones) físico o no físico

        Atributos: Son caracteristicas basicas del objeto, sean físicas o no físicas
        Metodos: son acciones que realiza un objeto (funcinamiento)

CLASE: nos ayuda a definir un objeto en concreto.
INSTANCIA: Nos ayuda a replicar los atributos y métodos de un objeto (clase).
"""
""" 
# Clase declarada
class Galleta:
    # Atributos
    forma = "Circular"
    peso = "15 gramos"
    textura = "Rugoso"
    olor = "Vainilla y canela"
    color = "Amarillo"
    sabor = "Vainilla"
    # Métodos(funcionalidades - funcion- acciones que realiza o se realiza con el objeto)
    def cantidad_de_galletas(self):
        print("La cantidad de galletas es 20.")

    def verificar_caducidad(self):
        print("Vencimiento el 25/12/2023")

# Programa principal

galleta1 = Galleta()
galleta1.cantidad_de_galletas()

print("**********************")

galleta2 = Galleta()
galleta2.verificar_caducidad()
"""

#PROGRAMA 02
# Elaborar una LI, con una clase Persona, la cual tiene como atributos el nombre, apellidos y el dni
# luego mostrar dicha información en pantalla mediante un método.

class Persona:

    def datos_persona(self, nombre, apellido, dni):
        self.nom = nombre
        self.ape = apellido
        self.dni = dni

    def imprimir_datos_persona(self):
        print(f"El nombre ingresado es {self.nom}, el apellido {self.ape} cuyo DNI es {self.dni}")

    
# PP
persona_1 = Persona()
persona_1.datos_persona("Luis", "Pineda", "12345678")
persona_1.imprimir_datos_persona()

print("************************************")

persona_2 = Persona()
persona_2.datos_persona("Carla", "Octavio" , "87546123")
persona_2.imprimir_datos_persona()


# Problema 03
# Elaborar una LI, que contenga una clase estudiante, que incluya los atributos:
# codigo, nombre, nota final del curso de python.
# Crear métodos, para sus atributos, otro método para imprimir los datos y finalmente
# uno para mostrar si el estudiante se encuentra aprobado.
# NOTA: mínimo aprobatorio es 11

class Estudiante:

    def guardarAtributos(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota

    def imprimirDatos(self):
        print(f"El código de estudiante es: {self.codigo}")
        print(f"El nombre de estudiante es: {self.nombre}")
        print(f"La nota final de estudiante es: {self.nota}")

    def mostrarEstado(self):
        if self.nota >= 11:
            print("ESTADO: Ud. se encuentra aprobado")
        else:
            print("ESTADO: Ud. se encuentra reprobado")

estudiante_1 = Estudiante()
estudiante_1.guardarAtributos(123456, "Juan Pineda", 16)
estudiante_1.imprimirDatos()
estudiante_1.mostrarEstado()

