# FUNCIONES - RETORNO DE DATOS
# Son las funcones que permiten recibir, operar y devolver datos.

# PROBLEMA 01:
# Elabora una lista de instruccines, que permita tener una funcion
# trapecio la cual devuelva el valir del área de dicha figura geométrica
"""
# FD
def area_trapecio(base_mayor, base_menor, altura):
    if base_mayor == base_menor:
        return "La pigura no es un trapecio"
    else:
        area_trapecio = ((base_mayor + base_menor) / 2) * altura
        return area_trapecio
    
# PP
base_mayor = int(input("Ingrese la base mayor del trapecio: "))
base_menor = int(input("Ingrese la base menor del trapecio: "))
altura = int(input("Ingrese la altura del trapecio: "))

area_final_trapecio = area_trapecio(base_mayor, base_mayor, altura)
print(f"El área del trapecio es : {area_final_trapecio:.2f}")
"""

# PROBLEMA 02
# Elaborar una LI, en la cual se envíe por teclado dos números
# y luego retorne el mayor de ambos en el prompt.

# FD
def retornar_mayor(numero1, numero2):
    if numero1 > numero2:
        numero_mayor = numero1
    else:
        numero_mayor = numero2
    
    return numero_mayor

# pp

print("Comparación de dos números enteros")

numero_1 = int(input("Ingrese un primer número : "))
numero_2 = int(input("Ingrese un segundo número : "))

print(f"El número mayor es: {retornar_mayor(numero_1, numero_2)}")