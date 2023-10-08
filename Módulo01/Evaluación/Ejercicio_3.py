horasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
costoXHora = float(input("Ingrese el costo por hora: "))
horasEstras = float(input("Ingrese la cantidad de horas extras trabajadas: "))

sueldoBase = horasTrabajadas * costoXHora
sueldoExtra = horasEstras * (costoXHora * 1.5)
sueldoTotal = sueldoBase + sueldoExtra

print(f"Sueldo base: {sueldoBase}")
print(f"Bono por horas extras: {sueldoExtra}")
print(f"Total por todas las horas de labor: {sueldoTotal}")