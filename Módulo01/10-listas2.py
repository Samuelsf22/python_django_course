# Problema 91
# Elaborar una LI, en la cual se tenga una lista con 7 número enteros.
# mostrar Ia sumatoria total de los números y su promedio.

"""
lista_numeros = [15, 20, 25, 35, 99, 79, 69]

suma = 0
i = 0
while i < len(lista_numeros):
    suma += lista_numeros[i]
    i = i + 1

promedio_numeros = suma / len(lista_numeros)
print(f"La lista esta compuesta por : {lista_numeros}")
print(f"La suma es: {suma}")                                    # 342
print(f"El promedio de los números es : {promedio_numeros}")    # 48.857142857142854
"""
# problema e2
# Elaborar una LI, en la cual se cuente con una lista vacia, que permita
# ingresar por teclado números a la lista, y luego imprima la lista completa.
"""
lista_numeros = []
cantidad_numeros = int(input("Cuántos números desea ingresar a la lista vacía: "))

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese un número entero {i+1}: "))
    lista_numeros.append(numero)

print(f"La lista de números ingresados es: {lista_numeros}")
"""
# PROBLEMA 03
# Elaborar una LI, en la cual se cuente con una lista vacía, la cual permita
# ingresar los sueldo de 7 trabajadores (floats) .
# Luego imprimir la suma total de los sueldos y el promedio global de los mismos.

lista_sueldos = []
for i in range(7):
    trabajador_sueldo = float(input(f"Ingrese el sueldo de trabajador {i+1}: "))
    lista_sueldos.append(trabajador_sueldo)
suma = 0
for i in range(len(lista_sueldos)):
    suma += lista_sueldos[i]

promedio_sueldos = suma / len(lista_sueldos)
print(f"La suma de los sueldos es : {suma}")
print(f"El promedio es {promedio_sueldos}")