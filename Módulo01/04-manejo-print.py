ciudad = "Huancayo"
pais = "Perú"

# IMPRESIÓN POR ARGUMENTOS MULTIPLES
print("Tu cuidad nata es : ", ciudad)
print("Tu pais de origen es : ", pais)
print("Me encanta", ciudad, "asi como mi", pais)

# IMPRESION POR FORMATO DE TIPO CADENA
print("Me encanta {} asi como mi {}".format(ciudad, pais))

# IMPRESION POR ARGUMENTO DE UNA TUPLA(es un elemento inmutable, desde una ruta externa)
print("Me encanta %s asi como mi %s" %(ciudad, pais))

#IMPRESION MEDIANTE FORMATE TIPO FSTRING
print(f"Me encanta {ciudad} asi como mi {pais}")