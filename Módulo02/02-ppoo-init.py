# método INIT (opcional)

# __init__, se inicializa cuando se crea una instacia, o se instancia un objeto, se crea un objeto.

# 1. Es el primer metodo a ejecutarse en una Li(cuando se crea una instencia u objeto)
# 2. Se autoinvoca, se inicaliza automáticamente.
# 3. Reemplaza a métodos iniciales recurrentes en una LI.
""" 
def __init__(self, parametros):
    Lista de intrucciones
"""

# Problema 01
# Elaborar una LI, con una clase trabajador, la cual contenga un método inicializador, con los atributos
# de nombre, apellido, cargo, sueldo, todos estos datos ingresador por teclado.
# Luego muestre en el prompt los datos ingresador y finalmente calcular cuanto es el descuento por AFP
"""
class Trabajador:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.cargo = input("Ingrese su cargo: ")
        self.sueldo = int(input("Ingrese su sueldo: "))

    def mostrarDatos(self):
        print(f"Su nombre es: {self.nombre}\nSu apellido es: {self.apellido}")
        print(f"Respecto a su cargo de {self.cargo}\nSu sueldo: {self.sueldo}")

    def descuentoAFP(self):
        self.descuento = self.sueldo * 0.13
        print(f"El descuento por AFP es : {self.descuento}")


trabajador01 = Trabajador()
trabajador01.mostrarDatos()
trabajador01.descuentoAFP()
"""

# Problema 02
# Elaborar una LI, en la cual se carguen dos números enteros utilizando el constructor init,
# luego calcular la suma, resta, división, multiplicación de los números enteros ingresador
# NOTA: cada operación debera estar en un método por separado
"""
class OperacionBasica:
    def __init__(self):
        self.numero1 = int(input("Ingrese un primer número entero: "))
        self.numero2 = int(input("Ingrese un segundo número entero: "))

    def suma(self):
        self.suma = self.numero1 + self.numero2
        print(f"La suma de los números es: {self.suma}")

    def resta(self):
        self.resta = self.numero1 - self.numero2
        print(f"La resta de los números es: {self.resta}")

    def division(self):
        self.division = self.numero1 / self.numero2
        print(f"La división de los números es: {self.division}")

    def multiplicación(self):
        self.multiplicación = self.numero1 * self.numero2
        print(f"La multiplicación de los números es: {self.multiplicación}")


operacion1 = OperacionBasica()
# operacion1.suma()
# operacion1.resta()

opcion = int(input("Elija una opción\n\t1. Suma\n\t2.Resta\n\t3. División\n\t4. Mutiplicación\nEjija una opcion del 1 al 4: "))

if opcion == 1 :
    operacion1.suma()
elif opcion == 2:
    operacion1.resta()
elif opcion == 3:
    operacion1.division()
elif opcion == 4:
    operacion1.multiplicación()
else:
    print("La opción es incorrecta")
"""
# Problema 03
# Elaborar una LI, en la cual se carguen dos números enteros utilizando el constructor init,
# luego calcular la division entera, resto, potenciacion de los números enteros ingresador
# NOTA: cada operación debera estar en un método por separado

class OperacionBasica:
    def __init__(self):
        self.numero1 = int(input("Ingrese un primer número entero: "))
        self.numero2 = int(input("Ingrese un segundo número entero: "))

    def divisionEntera(self):
        self.divisionEnter = self.numero1 // self.numero2
        print(f"La división entera de los números es: {self.divisionEnter}")

    def resto(self):
        self.rest = self.numero1 % self.numero2
        print(f"El resto de los números es: {self.rest}")

    def potencia(self):
        self.potencia = self.numero1 ** self.numero2
        print(f"La potencia de los números es: {self.potencia}")


operacion1 = OperacionBasica()
operacion1.divisionEntera()
operacion1.resto()
operacion1.potencia()

