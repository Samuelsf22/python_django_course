# Imprimir una cadena de texto
print("Hola, mundo")

# Imprimir múltiples argumentos separados por espacios
nombre = "Samuel"
edad = 20
print("Nombre:", nombre, "Edad:", edad)

# Usar formato de cadenas (f-strings) para interpolación de variables
nombre = "Medaly"
edad = 19
print(f"Mi nombre es {nombre} y tengo {edad} años.")

# Cambiar el separador entre argumentos utilizando el parámetro sep
colores = ["Rojo", "Verde", "Negro"]
print(colores, sep=", ")

# Imprimir en la misma línea utilizando el parámetro end
print("Hola", end=" ")
print("mundo!")

# Imprimir sin espacio entre argumentos utilizando el parámetro sep
print("Hola", "mundo", "de", "python", sep="")

# Imprimir el número con dos dígitos decimales
numero = 123.456789
print(f"Número formateado: {numero:.2f}")