cadena = input("Ingresa una cadena de texto: ")

longitud = len(cadena)

if 3 <= longitud < 10:
    print("Verdadero: esta en el rango")
else:
    print("Falso: fuera del rango")