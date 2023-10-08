# LLAMADA DE MÉTODOS

# Lo convencional

# class Persona:
#     pass
#     def ingresarNombres(self):
#         pass

# persona_1 = Persona()
# persona_1.ingresarNombres()
""" 
COMO INVOCAR UN MÉTODO DESDE OTRO MÉTODO.

self.nombre_del_metodo()
"""

# PROBLEMA 01
# Elaborar una LI, para hallar las áreas de las figuras geométricas (triángulo, rectángulo, cuadrado), para ello
# crear una clase area que solicite por teclado desde un "init" el ingreso de dos datos (base y la altura de la figura geométrica)
# Por cada tipo de área geometrica crear un método y llamarlos desde el método inicializador
""" 
class Area:
    def __init__(self):
        self.base = int(input("Ingrese la base de la figura: "))
        self.altura = int(input("Ingrese la altura de la figura: "))
        self.triangulo()
        self.rectangulo()
        self.cuadrado()
    
    def triangulo(self):
        self.area_triangulo = (self.base * self.altura) / 2
        print(f"El área del tringulo es: {self.area_triangulo}")
    
    def rectangulo(self):
        self.area_rectangulo = self.base * self.altura
        print(f"El área del rectangulo es: {self.area_rectangulo}")

    def cuadrado(self):
        if self.base == self.altura:
            self.area_cuadrado = self.base * self.altura
            print(f"El área del cuadrado es: {self.area_cuadrado}")
        else:
            print("La figura no es un cuadrado, sino un rectángulo")
    

area_1 = Area()

"""
# PROBLEMA 02
# Elaborar una LI, en la cual sea de realizar las opereraciones de potenciacion, redicacion
# por tal crear una clase por cada operacion, luego el programa debera permitir ingresar dos valores enteros
# a ser operados, todo desde la clase __init__, tambien debera contar con un menu de opciones a realizar desde el init.
# ejm:
# Elija una operacion:
# 1: Potenciacio
# 2: Radicación

class Potenciacion:
    def __init__(self):
        self.base = int(input("Ingrese la base: "))
        self.exponente = int(input("Ingrese el exponente: "))
        self.potencia()
    
    def potencia(self):
        print(f"La potencia es : {self.base ** self.exponente}")

class Radicacion:
    def __init__(self):
        self.num1 = int(input("Ingrese el radicando: "))
        self.num2 = int(input("Ingrese el índice: "))
        self.radicacion()

    def radicacion(self):
        print(f"La radicacion es : {self.num1 ** (1/self.num2)}")

class Operacion:
    def __init__(self):
        opcion = int(input("1: Potenciacion\n2: Radicación\nElija una opción: "))
        
        if opcion == 1:
            Potenciacion()
        elif opcion == 2:
            Radicacion()
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

Operacion()
        
