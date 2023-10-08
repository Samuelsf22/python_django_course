#TRABAJAR CON NUMEROS

val_1 = 5 #Entero

edad = 24 
#edad ) edad + 2
edad += 2

#edad ) edad - 6
edad-= 6

#edad = edad * 2
edad*=2

#edad = edad / 3
edad/=3

#edad = edad // 2 #division entero, es aquella que te devuele solo la parte entera
edad//=2

#edad = edad ** 2 #potencia
#edad**= 2
edad = pow(edad, 2)

print(edad)

print("*************")
##############################
#OPERACIONES CON FLOTANTES
estatura = 1.75

operacion0 = estatura / 2
operacion1 = estatura // 2
print(operacion0)
print(operacion1)

##############################
# CONVERSION DE TIPOS DE DATOS

# CONVERSION A ENTEROS
numero0 = int(7.57)
print(numero0)

numero1 = 1.75
conversion = int(numero1)
print(conversion)

num0 = input("Ingresa por favor un número ")
print(type(num0)) # todo lo que ingresa en un input es un String

num1 = int(input("Ingresa un numero "))
print(type(num1)) #ahora si es un entero (int)  

print("**************************")
#CONVERSION A FLOTANTES
numero2 = float(3)
print(numero2)
print(type(numero2))

numero3 = float('15.7')
numero4 = float('15.3')
suma = (numero3 + numero4)
print(suma)
print(type(suma))

numero5 = float(input("Ingrese el valor pi : "))
print(numero5)
print(type(numero5))

print("**************************")
#CONVERSION A BOOLEANO

#true = 1                // false = 0
#true => tiene contenido // false => no tiene contenido
variable = bool(90) #True
print(variable)
print(type(variable))

variable2 = bool(1) #True
print(variable2)
print(type(variable2))

variable3 = bool(0) #False
print(variable3)
print(type(variable3))

variable4 = bool("") #False
print(variable4)

variable5 = bool(" ") #True
print(variable5)