numero = int(input("Ingrese un número entero del 1 al 12: "))

if numero < 1 or numero > 12:
    print("El número debe estar en el rango del 1 al 12")
else:
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")
