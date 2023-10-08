# TUPLAS
# Son estructuras de datos que permiten crear grupos INMUTABLES de OBJEROS.
# Una vez creada NO SE PUEDE: Agregar, quitar, modificar.

dias_labarables = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

# OBTENER ELENENTOS
print(dias_labarables[0])
print(dias_labarables[4])

# PARA OBTENER LA POSICIÓN
print(dias_labarables.index("Martes"))
print(dias_labarables.index("Viernes"))

# BUSCAR CON UN ÍNDICE NEGATIVO
print(dias_labarables[-1])
print(dias_labarables[-5])

# DETERMINAR LA LONGITUD DE UNA TUPLA
print(len(dias_labarables))

# VERIFICAR SI UN ELEMENTO ESTÁ DENTRO DE UNA TUPLA
print("jueves" in dias_labarables)

# EXTRAER UNA POSICIÓN DE UNA TUPLA
print(dias_labarables[0:3]) # ('Lunes', 'Martes', 'Miercoles')
print(dias_labarables[0:5]) # ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')