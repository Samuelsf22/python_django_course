numerosIngresar = int(input("¿Cuántos números desea ingresar? : "))

sumaNumeros = 0

for i in range(numerosIngresar):
    numero = float(input(f"Ingrese un número {i+1}: "))
    sumaNumeros += numero

promedio = sumaNumeros / numerosIngresar

print(f"El promedio aritmético es: {promedio:.2f}")