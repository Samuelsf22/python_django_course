# + de 30 palabras claves

import keyword #importar las palabras reservadas de puthon
print(keyword.kwlist) #imprimir la lista de palabras reservajas

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Asignacion y variables

# Nombres de variables

x = 15
y = 25
varible_numerica = 2
nombre = "Luis"
apellido = "Cano"
nombreYapellido = "Luis Espinoza"
_apellido = "Espinoza" # No es recomendable usar esto
comunicacion = 15

############################################################
#Variables de tipo entero
numero_entero = 15
Numero_Entero = 30
suma_de_numeros = 500
sumaDeNumeros = 600

print(numero_entero)
print(Numero_Entero)
print(suma_de_numeros)
print(sumaDeNumeros)
print(numero_entero, Numero_Entero, suma_de_numeros, sumaDeNumeros)

############################################################
#variable de tipo cadena
cadena = 'Estudio python 3'
cadena_uno = 'Python \t para \t el \t mundo'
cadena_dos = 'Python \n es super \n fácil'
# \t para una tabilación
# \n  es para salto de linea

print(cadena)
print(cadena_uno)
print(cadena_dos)

############################################################
#VARIABLES DE TIPO FLOAT
print("************************")

numero_float1 = 3.141516
numero_float2 = 1.717271    #némero decimal
numero_float3 = 0.1e-5      #float con notacion científica
numero_float4 = 0x25        #numero hexadecimal
print(numero_float1)
print(numero_float2)
print(numero_float3)
print(numero_float4)
print(numero_float1, numero_float2, numero_float3, numero_float4)

############################################################
#VARIABLES TIPO BOOLEANO
print("************************")
booleano_verdadero = True
booleano_falso = False
negar_boleano = not booleano_falso #negacion de un boleano

print(booleano_verdadero)
print(booleano_falso)
print(negar_boleano)

############################################################
#VARIBALES TIPO COMPLEJAS
print("************************")
numero_complejo1 = 3 + 4j       #(3+4j)
numero_complejo2 = 5 + 4j*3     #(5+12j)

print(numero_complejo1)
print(numero_complejo2)

#determinar el tipo de dato que almacena una variable : type
print(type(numero_entero))
print(type(cadena))
print(type(numero_float1))
print(type(booleano_falso))
print(type(numero_complejo1))

############################################################
#OPERACIONES CON STRING (cADENAS DE CARACTERES)

apellido = "diario el peruano"
#IMPRIMIR EN MAYÚSCULAS
print(apellido.upper())

#LA LETRA INICIAL SOLO ESTE EN MAYÚSCULAS
print(apellido.capitalize())

#IMPRIMIR ALGO COMO SI FUERA UN TÍTULO
print(apellido.title())

#Buscando letras
#find devuelve la posición del valor buscado
print(apellido.find("e"))
print(apellido.find("ñ"))
print(apellido.find("z"))
print(apellido.find("ia"))

#SEPRARA CADENA DE CARACTERES
saludos = "Estamos practicando cadena de caracteres de manera practica"
#El split divide la cadena de texto en una lista y le asignara una posición
print(saludos.split())
print(saludos.split()[2]) #cadena
print(saludos.split()[0]) #Estamos

#CONTABILIZAR CADENA DE CARACTERES
print(saludos.count("a"))           #11
print(saludos.count("s"))           #3
print(saludos.count("ca"))          #4
print(saludos.count("practica"))    #2
   
print(saludos.__len__()) #59
print(len(saludos)) #devuelve el tamaño o longitud de una variable u objeto


print("*********************")
var_apellido = "Espinoza Alvarado Peinado"
print(type(var_apellido))
print(var_apellido.upper())
print(var_apellido.capitalize())
print(var_apellido.title())
print(var_apellido.find("o"))
print(var_apellido.find("za"))
print(var_apellido.split())
print(var_apellido.split()[1])  #Alvarado
print(var_apellido.split()[0])  #Espinoza
print(var_apellido.count("n"))  #2
print(var_apellido.count("a"))  #4
print(len(var_apellido))        #45