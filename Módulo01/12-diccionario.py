# DICCIONARIO
# Es una estructura de datos.
# Nos permite crear coleccines con un par clave/valot --- key/ValueError

# Key o clave, es INMUTABLE
# Value o el valor es MUTABLE

mascota_1 = {
    # KEY - VALUE
    'nombre': 'Scotty',
    'edad': 6,
    'raza' : 'pastor alemán'
}

print(mascota_1['nombre'])
print(mascota_1['edad'])
print(mascota_1['raza'])

print("**************************************")
# CAMBIANDO LOS VALORES
mascota_1['nombre'] = "Lazy"
mascota_1['edad'] = 5
mascota_1['raza'] = "doberman"

print(mascota_1['nombre'])
print(mascota_1['edad'])
print(mascota_1['raza'])

# VERIFICAR SI UNA KEY SE ENCUENTRA EN UN DICCIONARIO
print('raza' in mascota_1)

# AGREGAR UN NUEBO KEY / VALUE
mascota_1['Comida favorita'] = 'Carne de pollo'
print(mascota_1)

# ELIMINAR KEY / VALUE
del mascota_1['Comida favorita']
print(mascota_1)

# INVESTIGAR:
# MÉTODOS:

# get()          Es un método que se utiliza para acceder a elementos en un diccionario
#                de forma segura y evitar errores en caso de que la clave no exista

# pop()          Es un método que se utiliza para eliminar un elemento de un diccionario y devolver su valor asociado.

# popitem()      Se utiliza para eliminar el ultimo elemento ingresado

# keys()         Se utiliza para devolver una vista de todas las claves del diccionario.
#                La vista es un objeto iterable que contiene todas las claves del diccionario como una lista
