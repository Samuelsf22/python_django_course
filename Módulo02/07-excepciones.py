# EXCEPCIONES

# Son indicaciones que se producen luego de haber un error, al ejecutar un programa en específico,
# o cuando se termina de ejecutar un programa (genera una situacion no esperada)
""" 
try:
    LI de operaciones
except:
    LI que nos muestra el detalle del porque del error
"""

# Ejemplo 01
operacion01 = 1000 * 7 / 50
print(operacion01)

operacion02 = 1000 * (1 / 0)
print(operacion02)

# Ejemplo 02
edad = int(input("Ingrese su edad: "))
print(edad)

# Ejemplo 03
try:
    numero = int(input("Ingrese un número a ser divisor: "))
    operacionBase = 1000 * (2 / numero)
    print(operacionBase)
except ZeroDivisionError:
    print("No se puede dividir entre CERO, intente de nuevo.")

# Ejemplo 94
try:
    numero = input("Ingrese un número para dividir a 50: ")
    numero = int(numero)
    resultado = 50 / numero
    print(resultado)
except ZeroDivisionError:
    print("No se puede realizar una división entre cero.")
except ValueError:
    print("El valor no es válido")


# Ejemplo 05
repetir = True
while repetir:
    try:
        numero = int(input("Ingrese un número para dividir a 50: "))
        resultado = 50 / numero
        print(resultado)
        repetir = False
    except ZeroDivisionError:
        print("No se puede realizar una división entre cero.")
    except ValueError:
        print("El valor no es válido")

# Ejemplo 06
def mas_20(numero):
    return numero + 20

try:
    resultado = mas_20(80)
    print(resultado)
    myresultado = mas_20("ochenta")
except TypeError: 
    print("El argumento debe ser un número entero.")



