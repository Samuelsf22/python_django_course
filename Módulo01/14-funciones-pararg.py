# PARAMETROS: Es aquello que determina que va a permitir recibir una funcion.
# (ayuda a la función a recibir ciertos tipos y cantidad de datos) 

# ARGUMENTOS: Es es dato que se envía a la función.

# Ejemplo 01: 
"""
def saludoDeInicio(saludo_bienvenida):
    print(f"Bienvenido a python estimado {saludo_bienvenida}")

# PP
saludo = input("Ingrese un saludo complementario: ")
saludoDeInicio(saludo)
"""

# PROBLEMA 01
# Elaborar una LI, en la cual se realicen las operaciones de suma, resta y potenciación
# mediante parametros y argumentos,
# NOTA : Ingrear por cada operación dos valores por teclado
"""
# FD
def suma(valor1, valor2):
    suma = valor1 + valor2
    print(f"La suma de los valores es: {suma}")

def resta(valor1, valor2):
    resta = valor1 - valor2
    print(f"La resta de los valores es: {resta}")

def potencia(valor1, valor2):
    potencia = valor1 ** valor2
    print(f"La potencia de los valores es: {potencia}")

# PP

print("************SUMA************")
print("Ingrese dos números a sumar: ")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
suma(numero1, numero2)


print("************RESTA************")
print("Ingrese dos números a restar: ")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
resta(numero1, numero2)


print("**********POTENCIA***********")
print("Ingrese dos números a rezlizar potencia: ")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
potencia(numero1, numero2)
"""

# PROBLEMA PROPUESTO
# Elabora una LI, en la cual se realicen las operaciones de:
# *, /, //, % a traves de funciones con parametros y argumentos,
# las cuales soliciten ingresar un par de datos generales para todas
# estas operaciones 

"""
def multiplicacion(valor1, valor2):
    return valor1 * valor2

def division(valor1, valor2):
    return valor1 / valor2

def division_entera(valor1, valor2):
    return valor1 // valor2

def modulo(valor1, valor2):
    return valor1 % valor2

print("Ingrese dos números : ")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

multiplicacion = multiplicacion(numero1, numero2)
division = division(numero1, numero2)
division_entera = division_entera(numero1, numero2)
modulo = modulo(numero1, numero2)

print(f"La multiplicación de los valores es: {multiplicacion}")
print(f"La división de los valores es: {division:.2f}")
print(f"La división entera de los valores es: {division_entera}")
print(f"El módulo de los valores es: {modulo}")
"""

# PROBLEMA 04
# Elaborar una LI, en la cual nos pida una base y una altura de una figura geométrica
# luego que nos permita elegir entre un par de opciones Triangulo (1) rectangulo(2), y luego nos muestre
# medienta el prompt el valor de la superficie de la figura-

# FD
def area_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    print(f"El área del triángulo es: {area_triangulo:.2f} unidades cuadradas")

def area_rectangulo(base, altura):
    area_rectangulo = base * altura
    print(f"El área del rectángulo es: {area_rectangulo:.2f} unidades cuadradas")

opcion = int(input(f"Área geometrica :\nTriángulo : 1\nRectángulo : 2\nElija una opción (1 ó 2): "))

if opcion == 1 or opcion == 2:
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))

    if opcion == 1:
        area_triangulo(base, altura)
    if opcion == 2:
        area_rectangulo(base, altura)
else:
    print("Opción incorrecta")