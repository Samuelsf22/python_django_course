# WHILE (ESTRUCTURA REPETITIVA)
# Nos permite ejecutar una LI, previa verificación de una condición dada.
"""
while condición:
    Lista de intrucciones
otras listas de intrucciones
"""

# PROBLEMA 01
# Elaboremos un LI, que nos permita en el prompt los 50
# primeros números
"""
variable = 1
while variable <= 50 :
    print(variable)
    variable += 1 
"""

# PROBLEMA 02
# Elaborar una LI, que permita ingresar un entero, e imprima
# desde cero hasta dicho valor
"""
valor_entero = int(input("Ingrese un número entero: "))

valor = 0
while valor <= valor_entero:
    print(valor)
    valor += 1
"""

# PROBLEMA 03 
# Mostrar en el prompt, los numeros de 100 al 500
# Mostrar en el prompt, los numeros de 19 al 99
# Mostrar en el prompt, los numeros de 50 al 200 (solo pares) 
"""
valor = 100
while 100 <= valor <= 500:
    print(valor)
    valor += 1

valor_2 = 19
while 19 <= valor_2 <= 99:
    print(valor_2)
    valor_2 += 1
    
valor_3 = 50
while 50 <= valor_3 <= 200:
    if valor_3 % 2 == 0:
        print(valor_3)
    valor_3 += 1 
"""

# PROBLEMA 04
# Elaborar una Li, en la cual se ingrese las 4 calificaciones de un estudiante del curso de python.
# luego muestre en el prompt la suma de notas y el promedio final de las mismas, mediante la utilización del while.

contador = 1
suma_notas = 0

while contador <= 4:
    nota = int(input(f"Ingrese la nota {contador}: "))
    suma_notas += nota
    contador += 1

promdio_notas = suma_notas / 4
print(f"La suma de notas es : {suma_notas}")
print(f"El promedio final de notas es: {promdio_notas}")
