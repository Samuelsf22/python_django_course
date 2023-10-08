# LISTA
# Son una estructura escencial de datos en python. Colección.
# Permite agrupar, varios valores (diferenctes tipos de datos) a lso que haga referencia el nombre de la lista.

perros = ["Scoty", "Lucas", "Bellas", "Peluza", "Shadow"]

precios_platos_tipicos = ["Ceviche", 35, "Pachamanca", 28, "Lomo Saltado", 35.5, "Ají de Gallina", False]


# LISTA DE EJEMPLO: 
articulo_limpieza = ["Detergente", 6, "Jabón", 4.50, "Shampoo", True]

# vERIFICAR SI UN ELEMENTO SE ENCUENTRA EN LA LISTA
print("Shampoo" in articulo_limpieza)
print("Ayudin" in articulo_limpieza)

# CÓNO DEFINIMOS UNA LISTA VACÍA
articulo_limpieza_2 = []

# HACER REFERENCIA A UN ELEMENTO DE LA LISTA
articulo_limpieza[0] # DETERGENTE
articulo_limpieza[2] # JABÓN
articulo_limpieza[4] # SHAMPOO

# IMPRIMIR ELEMENTOS 
print(articulo_limpieza[0]) # DETERGENTE
print(articulo_limpieza[2]) # JABÓN
print(articulo_limpieza[4]) # SHAMPOO

# AHORA REEMPLAZAMOS VALORES
articulo_limpieza[0] = "Lejía"
print(articulo_limpieza)
print(articulo_limpieza[0])

# COMO SABER LA POSICION DONDE SE ENCUENTRA UN ELEMENTO EN LA LISTA
print(articulo_limpieza.index("Shampoo")) # 4
print(articulo_limpieza.index("Jabón"))   # 2
print(articulo_limpieza.index(1))         # 5

# COMO PODEMOS IMPRIMIR ELEMENTOS CON INDICE NEGATIVO
# articulo_limpieza = ["Lejía",  6, "Jabón", 4.50, "Shampoo", True]
# articulo_limpieza = [     -6, -5,      -4,   -3,        -2,  -1 ]
print(articulo_limpieza[-1]) # True
print(articulo_limpieza[-3]) # 4.5

# PODEMOS EXTRAER DE UNA LISTA UNA PORCIÓN, CON SLICES
print(articulo_limpieza[0:2]) # ['Lejía', 6]
print(articulo_limpieza[2:5]) # ['Jabón', 4.5, 'Shampoo']

# PODEMOS DEREMINAR LA LONGITUD DE UNA LISTA - DETERMINAT NTO DE ELEMENTOS DE UNA LISTA
len(articulo_limpieza)          #6
print(len(articulo_limpieza))

# AGREGAR ELEMENTOS A UNA LISTA append(), AGREGA AL FINAL DE LA LISTA UN ELEMENTO
articulo_limpieza.append("Detergente")
articulo_limpieza.append(4.5)
print(articulo_limpieza) # ['Lejía', 6, 'Jabón', 4.5, 'Shampoo', True, 'Detergente', 4.5]

# PARA GUARDAR VARIOS CARACTERES
articulo_limpieza.extend(["DEMO"])
articulo_limpieza.extend("DEMO") #DEBES USAR CORCHETE, sino lo separá por caracteres ('D', 'E', 'M', 'O')
print(articulo_limpieza)

articulo_limpieza += ["ABC"]
articulo_limpieza += "ABC"
print(articulo_limpieza)

# ELIMINACIÓN DE ELEMENTOS
articulo_limpieza.remove("DEMO")
borrar1 = input("Ingrese el elemento a eliminar: ")
articulo_limpieza.remove(borrar1)
print(articulo_limpieza) # ['Lejía', 6, 'Jabón', 4.5, 'Shampoo', True, 'Detergente', 4.5, 'D', 'E', 'M', 'O', 'A', 'B', 'C']

# AÑADIR ELEMTNOS EN UN INDICE EN ESPECÍFICO CON insert()
articulo_limpieza.insert(1, 4)
print(articulo_limpieza)

articulo_limpieza.insert(2, "Escobilla")
print(articulo_limpieza)