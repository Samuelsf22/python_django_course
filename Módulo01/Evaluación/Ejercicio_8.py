def registrarBloque():
    pedidos = int(input("Ingrese la cantidad de bloques de tela en el lote: "))
    bloques = []

    for i in range (pedidos):
        bloque = float(input((f"Ingrese la longitus del bloque {i+1}: ")))
        bloques.append(bloque)

    return bloques


def aptos(bloques):
    contador = 0

    for i in range(len(bloques)):
        if 150 <= bloques[i] <= 300:
            contador += 1

    return contador


bloques = registrarBloque()
contadorAptos = aptos(bloques)

print(f"La cantidad de bloques de tela aptos para procesar es: {contadorAptos}")
