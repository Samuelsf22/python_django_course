#INGRESAR POR TECLADO
"""
apellido = input("Ingrese tu apellido : ")
nombre = input("Ingrese su nombre : ")
"""

#PROBLEMA 01
# Elaborar una LI, en la cual se ingrese tres numeros
# para Luego sumarlos y luego multiplicarlos, finalmente
# mostrar el resultado de cada operacion en el prompt.

"""
numero1 = int(input("Ingresa el primer número : "))
numero2 = int(input("Ingresa el segundo número : "))
numero3 = int(input("Ingresa el tercer número : "))
suma = numero1 + numero2 + numero3
multiplicacion = numero1 * numero2 * numero3

print("La suma de los nñumeros es : ", suma)
print("La multiplicacion de los numeros es : ", multiplicacion)
"""

# PROBLEMA 02
# Elabora una LI, en la cual se ingres una cantidad de productos
# para obtener el costo total, respecto al precio que se tiene por unidad
# de dicho producto.
"""
cantidad_producto = int(input("Ingresa la cantidad de productos a llevar : "))
precio = float(input("Ingrese el precio unitario del producto a llevar"))

costo_total = cantidad_producto * precio
precio("El costo totla a pagar es de : ", costo_total)
"""
# PROBLEMA 03
#Elaborar una LI, en la cual traves del teclado se ingrese el lado DE un cuadrado,
# luego muestre en el prcmpt, el perimetro y el área.

"""
lado_cuadrado = int(input("Ingrese el lado del cuadrado: "))
perimetro_cuadrado = lado_cuadrado * 4
area_cuadrado = lado_cuadrado ** 2
print("El perimetro del cuadrado es : ", perimetro_cuadrado)
print("El área del cuadrado es: ", area_cuadrado, "metros cuadrados")
"""
# PROBLEMA 04
# Elabora una LI que permite ingresar por teclado cinco calificaciones de un estudiante python,
# Luego muestre en el prompt la suma total de las misma y el promedio final

"""
calif_01 = int(input("Ingrese la calificación 01: "))
calif_02 = int(input("Ingrese la calificación 02: "))
calif_03 = int(input("Ingrese la calificación 03: "))
calif_04 = int(input("Ingrese la calificación 04: "))
calif_05 = int(input("Ingrese la calificación 05: "))

suma_total = calif_01 + calif_02 + calif_03 + calif_04 + calif_05

promedio_final = suma_total / 5

print("La suma total de notas es: ", suma_total, "y el promedio final es: ", promedio_final) 
"""

# PROBLEMA 05
# Luis Trabaja en una fabrica al mes unas 15 horas recibe por hora S/ 30.
# Carlos Trauejg en la misma fabrica realizando unas 25 horas por que recibe S/ 50 per hora.
# Determinar cuanto es el sueldo de luis y carlos al mes, y luego mostrar la suma


horasLuis = 15
pagoLuis = 30

horasCarlos = 25
pagoCarlos = 50

sueldoLuis = horasLuis * pagoLuis
sueldoCarlos = horasCarlos * pagoCarlos

sumaSueldos = sueldoLuis + sueldoCarlos

print("El sueldo de Luis al mes: S/ ", sueldoLuis)
print("El sueldo de Carlos al mes: S/ ", sueldoCarlos)
print("La suma de los sueldos es: S/ ", sumaSueldos)