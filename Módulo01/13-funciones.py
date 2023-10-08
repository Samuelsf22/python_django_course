# FUNCIONES

# Es un conjunto de instrucciones (LI) que nos va a permitir resolver
# un problema en concreto, respecto a uno más grande preexistente

# EJEMPLO
# Realizar el saludos de bienvenida.
"""
# Funciones definidas (FD)
def saludoBienvenida():
    print("*********************************")
    print("*Hola mundo python con Funciones*")
    print("*********************************")


# Programa principal (PP)
saludoBienvenida()
"""

# Ejemplo 02
# Realizar Ia suma de tres numero enteros con funciones.
"""
# FD
def sumaDenumeros() :
    numero_1 = int(input("Ingrese un primer número: "))
    numero_2 = int(input("Ingrese un segundo número: "))
    numero_3 = int(input("Ingrese un tercer número: "))
    suma_total = numero_1 + numero_2 +numero_3
    print(f"La suma total de los números es : {suma_total}")
# PP
sumaDenumeros()
"""

# PROBLEMA 01
# Elaborar un LI, en la cual se tenga operaciones de suma, resta, las cuales
# recepcione dos números enteros por cada una, las opere y las muestre con sus
# respectivos resultados en el prompt.
"""
# FD
def sumaDeNumeros():
    print("******** SUMA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    suma = numero_1 + numero_2
    print(f"La suma de números es : {suma}")

def restaDeNumeros():
    print("******** RESTA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    resta = numero_1 - numero_2
    print(f"La suma de números es : {resta}")
# PP
sumaDeNumeros()
restaDeNumeros()
"""

# PROBLEMA 02
# Elaborar una LI, en la cual se realicen las operaciones de
# +, -, *, /, //, %, ** a travez de funcinoes, las cuales
# soliciten ingresar un par de datos enteros por cada una de ellas 
# y finalmente muestren el resultado en el prompt

def suma():
    print("******** SUMA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    suma = numero_1 + numero_2
    print(f"La suma de números es : {suma}")

def resta():
    print("******** RESTA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    resta = numero_1 - numero_2
    print(f"La resta de números es : {resta}")

def multiplicacion():
    print("******** MULTIPLICACIÓN DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    multiplicacion = numero_1 * numero_2
    print(f"La multiplicacion de números es : {multiplicacion}")

def division():
    print("******** DIVISIÓN DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    división = numero_1 / numero_2
    print(f"La división de números es : {división}")

def division_entera():
    print("******** DIVISIÓN ENTERA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    division_entera = numero_1 // numero_2
    print(f"La división entera de números es : {division_entera}")

def resto():
    print("******** RESTO DE LA DIVISIÓN DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    resto = numero_1 % numero_2
    print(f"El resto de la división de números es : {resto}")

def potencia():
    print("******** POTENCIA DE NÚMEROS ********")
    numero_1 = int(input("Ingrese un primer número : "))
    numero_2 = int(input("Ingrese un segundo número : "))
    potencia = numero_1 ** numero_2
    print(f"La potencia de números es : {potencia}")

suma()
resta()
multiplicacion()
division()
division_entera()
resto()
potencia()
