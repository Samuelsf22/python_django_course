def operaciones(valores):
    contarNegativos = 0
    contarPositivos = 0
    contarM15 = 0
    sumaPares = 0

    for valor in valores:
        if valor < 0:
            contarNegativos += 1
        elif valor > 0:
            contarPositivos += 1

        if valor % 15 == 0:
            contarM15 += 1

        if valor % 2 == 0:
            sumaPares += valor

    return contarNegativos, contarPositivos, contarM15, sumaPares


valores = []
for i in range(10):
    valor = int(input(f"Ingrese un número entero {i+1}: "))
    valores.append(valor)

contarNegativos, contarPositivos, contarM15, sumaPares = operaciones(valores)

print(f"Cantidad de valores negativos: {contarNegativos}")
print(f"Cantidad de valores positivos: {contarPositivos}")
print(f"Cantidad de múltiplos de 15: {contarM15}")
print(f"Suma total de números pares: {sumaPares}")