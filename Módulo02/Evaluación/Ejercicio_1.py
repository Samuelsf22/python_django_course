def tablaMultiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


try:
    numero = int(input("Ingrese el número para la tabla de multiplicar (hasta 12): "))
    if numero <= 12:
        tablaMultiplicar(numero)
    else:
        print("El límite debe ser 12 o menos.")
except ValueError:
    print("Por favor, ingrese un número válido.")