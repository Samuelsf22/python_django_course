# CONDICIONALES SIMPLES
# Son aquellas que nos permiten tomar una eleccion respecto a una sola condición.

# Si es verdadero, se ejecutara la lista de intrucciones, caso contrario no se se ejecutará nada
"""
if condicion:
    Lista de instrucciones
"""
# PROBLEMA 01
# Elaborar una LI, la cual permita tener sueldo de un trabajador,
# el cual labora de lunes a viernes 8 horas y los sábados 4 horas, (ganando 35xhora)
# si el sueldo llegara a superar los S/1500, mostrar en pantalla, cuanto debe pagar de impuestos
"""
sueldoMes = 8 * 35 * 4 + 4 * 35 * 4
if sueldoMes > 1500:
    impuesto = sueldoMes * 0.08
    print("El impuesto a pagar es: ", impuesto) 
print("Ud. no ha de pagar impuesto.")
"""

######################################################################################
# CONDICIONALES COMPUESTAS
# Es en la cual tenemos dos caminos uno de verdadero y otro falso.
# por ceda camino se ejecuta una lista de instrucciones, pero jamas se ejecutan ambas.

"""
if condicion:
    lista de instrucciones
else:
    lista de instrucciones
"""

# PROBLEMA 02
# Elabora una LI, en la cual se ingrese por teclado dos numero enteros diferentes
# luego que se muestre en pantalla el mayo de ellos
"""
numero01 = int(input("Ingresa el primero número: "))
numero02 = int(input("Ingresa el segundo número: "))
if numero01 > numero02:
    print("El numero mayor es: ", numero01)
else:
    print("El número mayor es: ", numero02)
"""

######################################################################################
# OPERADORES MATEMÁTICOS: +, -, /, //, **, %
# OPERADORES RELACIONALES: ==, !=, <, >, <=, >=

# PROBLEMA 03
# Elaborar una LI, en la cual se cargue dos números diferente por teclado,
# Si el primer número resulta ser el mayor, imprimir en pantalla la suma y resta de dichos números
# caso contrario imprimir el producto y la division del primero respecto al segundo número
"""
numeroUno = int(input("Ingrese el número 1: "))
numeroDos = int(input("Ingrese el número 2: "))

if numeroUno > numeroDos : 
    print("La suma es : ", numeroUno + numeroDos)
    print("La resta es : ", numeroUno - numeroDos)
else: 
    print("El producto es : ", numeroUno * numeroDos)
    print("La división es : ", numeroUno / numeroDos)
"""

######################################################################################
#CONDICIONAL SELECTIVA - COMPUESTA, DOBLE, ANIDADA, MULTIPLE
"""
numero01 = int(input("Ingresa el primero número: "))
numero02 = int(input("Ingresa el segundo número: "))
if numero01 > numero02:
    print("El numero mayor es: ", numero01)
elif numero01 == numero02:
    print("Ambos números son iguales")
else : 
    print("El número mayor es: ", numero02)
"""

# PROBLEMA 05
# Elaborar una LI, en la cual se ingrese por teclado 4 calificaciones de un estudiante de python
# luego de calcular el promedio final y segun el resultado mostrar en el prompt lo siguiente acorde a :
# Si el promedio final es >= 16 mostrar en el prompt "Estudiante Destacado"
# Si el promedio final es >= 11 y <= 15 mostrar en el propmt "Estudiante Regular"
# Si el promedio final es <11 en el prompt "Estudiante desaprobado"
"""
calif01 = int(input("Ingrese la primera calificación: "))
calif02 = int(input("Ingrese la segunda calificación: "))
calif03 = int(input("Ingrese la tercera calificación: "))
calif04 = int(input("Ingrese la cuarta calificación: "))

promedioFinal = (calif01 + calif02 + calif03 + calif04)/4
if promedioFinal >= 16:
    print("Ud. es un estudiante destacado, con la calificación de : ", promedioFinal)
else:
    if promedioFinal >= 11:
        print("Ud. es un estudiante regular, con la calificación de : ", promedioFinal)
    else : 
        print("Ud, estudiante ha desaprobado, con la calificación de : ", promedioFinal)
"""

# PROBLEMA 06
# elaborar una LI, en la cula se ingrese tres números enteros diferentes, 
# luego mostrar en el prompt, cual de ellos es el número mayor

numero_1 = int(input("Ingrese un primer número: "))
numero_2 = int(input("Ingrese un seugndo número: "))
numero_3 = int(input("Ingrese un tercer número: "))
"""
if numero_1 > numero_2:
    if numero_1 > numero_3:
        print("El número mayor es: ", numero_1)
    else:
        print("El número mayor es: ", numero_3)
else:
    if numero_2 > numero_3:
        print("El numero mayor es el: ", numero_2)
    else:
        print("El número mayor es: ", numero_3)
"""

if numero_1 == numero_2 == numero_3:
    print("Los números son iguales")
else:
    if numero_1 > numero_2:
        if numero_1 > numero_3:
            print("El número mayor es: ", numero_1)
        else:
            print("El número mayor es: ", numero_3)
    else:
        if numero_2 > numero_3:
            print("El numero mayor es el: ", numero_2)
        else:    
            print("El número mayor es: ", numero_3)