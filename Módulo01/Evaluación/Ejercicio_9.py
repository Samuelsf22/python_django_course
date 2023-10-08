def añadirRecaudacion(numRecaudacion):
    recaudacion = {}
    print(f"Ingrese los valores de la recaudación {numRecaudacion}:")

    for i in range(15):
        valor = float(input(f"Ingrese el valor {i + 1}: "))
        recaudacion[i] = valor

    return recaudacion

recaudacion1 = añadirRecaudacion(1)
recaudacion2 = añadirRecaudacion(2)

totalR1 = sum(recaudacion1.values())
totalR2 = sum(recaudacion2.values())

if totalR1 > totalR2:
    diferencia = totalR1 - totalR2
    mensaje = "La recaudación 1 tiene un mayor monto acumulado."
elif totalR2 > totalR1:
    diferencia = totalR2 - totalR1
    mensaje = "La recaudación 2 tiene un mayor monto acumulado."
else:
    diferencia = 0
    mensaje = "Ambas recaudaciones tienen el mismo monto acumulado."

print(mensaje)
print(f"Diferencia de montos: {diferencia}")
