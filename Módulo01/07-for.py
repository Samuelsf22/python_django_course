# Estructura for (Iterativa, Repetitiva)

# Es una estructura qye permite realizar una LI una cierta cantidad de veces,
# las cuales son repetitivas y de forma limitada
"""
for rango:
    Lista de Intrucciones
"""

"""
lista = [87, 5, 2, 1, 4, 3, "Hola", "Adiós", "Carla", 0.9]
print(len(lista))

for x in lista:
    print("Hola a todos en el mundo Python")

for x in [87, 5, 2, 1, 4, 3, "Hola", "Adiós", "Carla", 0.9]:
    print(f"Elemnto {x}")

for x in (8, 9, 3, 2, 3.141516):
    print(f"Elemento{x}")
"""

# PROBLEMA 01
# Elaborar una LI que imprima los 50 primeros números

# va a recorrer hasta que el rango sea uno menor, algo asi x < 51, solo llegaría al 50
"""
for x in range(51):
    print(f" Impresiñon del número {x}")
"""

# PROBLEMA 02
# Elaborar un LI, en la cula se imprima en el prompt los números entre 100 y 199

#al menor no se le quita nada, al mayor si se le quita 1
"""
for x in range(100, 200):
    print(f"Número: {x}")
"""

# PROBLEMA 03
# Elaborar una LI, la cual permita imprimir en el prompt, los números impares entre 300 y 400

# 301 = min, 400 = max - 1, 2 = salto (de 2 en 2) 
"""
for x in range(301, 400, 2):
    print(f"Los números impares son {x}")
"""

# PROBLEMA 04
# Elaborar una LI, en cual permitar carga 4 calificaciones de una estudiante del curso de Python
# por teclado, luego muestre en el prompt la suma total de calificaciones así como el promedio final

#Si solo pones el valor maximo comienza desde el 0
"""
suma_notas = 0
for x in range(4):
    nota = int(input(f"Ingrese la nota a promediar {x+1}: "))
    suma_notas += nota
promedio_final = suma_notas / 4
print(f"La sumatoria total de notas es: {suma_notas}")
print(f"El promedio final es : {int(promedio_final)}")
"""

# PROBLEMA 05
# Un estudiante de un colegio del centro, tiene los curso de:
# aritm´rtica, algebra, geometria, tringonomiatria, física, química, comunicación e historia.
# Elaborar una LI, que permita ingresar por teclado las calificaciones de lso cursos mencionados
# y luego infomr cuántos han aprobado el estudiante (ntoas mayores o iguales a 11) y cuantos
# cursos tiene desarprobado (notas menores o igual a 10)
"""
nota_aprob = 0
nota_desap = 0

for x in ("Aritmética", "Algebra", "Geometría", "Trigonometría", "Física", "Química", "Comunicación", "Historia"):
    nota = int(input(f"Ingrese la nota de {x}: "))
    if nota >= 11:
        nota_aprob += 1
    else:
        nota_desap += 1

print("La cantidad de cursos Aprobados es: ", nota_aprob)
print("La cantidad de cursos desaprobados es: ", nota_desap)
"""

# PROBLEMA 06
# Elaborar una LI que nos permita ingresar mediante el prompt una cantidad "n" de números
# que nosotros mismos indiquemos, para posteriormente nos muestre en el prompt,
# cuantos de estos numeros ingresados son mayores a 99.
"""
cantidad_ingresar = int(input("¿Cúantos números desea ingresar: ?"))
contador = 0 
for x in range(cantidad_ingresar)
    numero = int (input("Ingrese un número entero: "))
    if numero > 99:
        contador += 1

print(f"La cantidad de números mayor es a 99 es: {contador}")
"""

# PROBLEMA 07
# Elaborar una LI en la cual permita ingresar 13 números enteros, luego
# que se pueda indentificar cuantos son multiplos de 3 y cuantos son multiplos  de 5.
# dichos resultados se debran mostrar en el prompt.

multiplos_tres = 0
multiplos_cinco = 0

for x in range(13):
    numero = int(input(f"Ingrese un número entero {x+1}: "))
    if numero % 3 == 0:
        multiplos_tres += 1
    if numero % 5 == 0:
        multiplos_cinco += 1

print(f"Multiplos de 3: {multiplos_tres}")
print(f"Multiplos de 5: {multiplos_cinco}")

