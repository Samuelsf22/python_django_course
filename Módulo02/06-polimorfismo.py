# POLIMORFISMO
# PPOO -- > Sobrecarga de métodos, cuando se utilizan diversas instancias, se obtiene resultados diferentes
# con un mismo método (con una sobrecarga de métodos)


# Ejemplo 1
""" 
class Persona:
    def __init__(self):
        self.nombre = "Milagros"
        self.dni = 41256378

    def mensaje(self):
        print(f"Hola, {self.nombre} tu DNI es {self.dni}")

class Trabajador(Persona):
    def __init__(self):
        self.cargo = "Developer"
        self.sueldo = 3500

    def mensaje(self):
        print(f"Este mensaje viene de la clase trabajador.")
        print(f"Usted como {self.cargo} gana un promedio de {self.sueldo}")
    

Trabajador1 = Persona()
Trabajador1.mensaje()

print("******************")

Trabajador2 = Trabajador()
Trabajador2.mensaje()
"""


# Ejemplo 2
""" 
class Gato:
    def hablar(self):
        print("Miau Miau :D")


class Perro(Gato):
    def hablar(self):
        print("Guau, Guau :D")


def escucharMascotas(animal):
    animal.hablar()


miMascota = Gato()
escucharMascotas(miMascota)

print("-********************")

miMascota = Perro()
escucharMascotas(miMascota)
"""

# Problema 01:
# Elaborar una LI, en la cual se cuente con dos clases, jefeDeEquipo y colaborador, los cuales
# tienen iniciadores, el primero con los datos del nombre, dni , sueldo, y el segundo: nombre, dni, cargo, sueldo.
# ambas clases tendran un método en común llamado "mensaje", dicho Método debera de mostrar en pantalla cuanto
# recibira como sueldo final, si este método tiene como parámetro la cantidad de clientes atendidos.
# NOTA: El jefe ganará 20% adicional y el colaborador recibira 10% en caso la calidad de clientes supere los 30 clientes atendidos.
# Utilizar concepto de polimorfismo entendiendo que el colaborador hereda de jedeDeEquipo.
""" 
class JefeEquipo:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del jefe de equipo: ")
        self.dni = int(input("Ingrese el DNI del jefe de equipo: "))
        self.sueldo = int(input("Ingrese el sueldo del jefe de equipo: "))

    
    def mensaje(self, cantidad_clientes):
        if cantidad_clientes > 30:
            self.sueldo_final = self.sueldo * 1.20
            print(f"El jefe de equipo ha de ganar: {self.sueldo_final}")
        else: 
            print(f"el jefe de equipo ha de ganar: {self.sueldo}")

class Colaborador(JefeEquipo):        
    def __init__(self):
        self.nombre = input("Ingrese el nombre del colaborador: ")
        self.dni = int(input("Ingrese el DNI del colaborador: "))
        self.cargo = input("Ingrese el cargo del colaborador: ")
        self.sueldo = int(input("Ingrese el sueldo del colaborador: "))
    
    
    def mensaje(self, cantidad_clientes):
        if cantidad_clientes > 30:
            self.sueldo_final = self.sueldo * 1.10
            print(f"El jefe de equipo ha de ganar: {self.sueldo_final}")
        else:
            print(f"El jefe de equipo ha de ganar {self.sueldo}")


colaborador1 = JefeEquipo()
colaborador1.mensaje(35)
print("*****************")
colaborador2 = Colaborador()
colaborador2.mensaje(5)
"""

# Variación del problema anterior
""" 
class JefeEquipo:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del jefe de equipo: ")
        self.dni = int(input("Ingrese el DNI del jefe de equipo: "))
        self.sueldo = int(input("Ingrese el sueldo del jefe de equipo: "))

    
    def mensaje(self, cantidad_clientes):
        if cantidad_clientes > 30:
            self.sueldo_final = self.sueldo * 1.20
            print(f"El jefe de equipo ha de ganar: {self.sueldo_final}")
        else: 
            print(f"el jefe de equipo ha de ganar: {self.sueldo}")

class Colaborador(JefeEquipo):        
    def __init__(self):
        self.nombre = input("Ingrese el nombre del colaborador: ")
        self.dni = int(input("Ingrese el DNI del colaborador: "))
        self.cargo = input("Ingrese el cargo del colaborador: ")
        self.sueldo = int(input("Ingrese el sueldo del colaborador: "))
    
    
    def mensaje(self, cantidad_clientes):
        if cantidad_clientes > 30:
            self.sueldo_final = self.sueldo * 1.10
            print(f"El jefe de equipo ha de ganar: {self.sueldo_final}")
        else:
            print(f"El jefe de equipo ha de ganar {self.sueldo}")

def llamarMetodo(objeto, cantidad_clientes):
    objeto.mensaje(cantidad_clientes)

colaborador1 = JefeEquipo()
llamarMetodo(colaborador1, 23)
print("*****************")
colaborador2 = Colaborador()
llamarMetodo(colaborador2, 32)
"""

# Problema 02:
# Elaborar una LI, en la cual se cuente con dos clases que representen a un editor y a un escritor,
# cada clase, deberá de tener los datos principales del personal(apellidos, nombres, edad, dni, nroClientes), todo ello ingresando desde teclado(no utilizar método inicializador)
# Luego cada clase debera de contar con un método llamado bono el cual permita mencionar si el personal recibirá un pago adicional como bono o no
# NOTA: nroClientes, se refiere a la cantidad de personas atendidas en un mes.
# si la cantiadad supera los 40, mostrat un mensaje si el personal recibira un bono extra.
# del mismo modo su el escritor supera los 3 libros.
""" 
class Editor:
    def datos(self):
        self.apellidos = input("Ingrese sus apellidos: ")
        self.nombres = input("Ingrese sus nombres: ")
        self.edad = int(input("Ingrese su edad: "))
        self.dni = input("Ingrese su DNI: ")
        self.nroClientes = int(input("Ingrese el número de clientes atendidos en el mes: "))

    def bono(self):
        if self.nroClientes > 40:
            print(f"{self.nombres}, usted recibirá este mes su bono")
        else:
            print(f"{self.nombres}, este mes usted no aplica al bono.")

class Escritor:
    def datos(self):
        self.apellidos = input("Ingrese sus apellidos: ")
        self.nombres = input("Ingrese sus nombres: ")
        self.edad = int(input("Ingrese su edad: "))
        self.dni = input("Ingrese su DNI: ")
        self.nroLibros = int(input("Ingrese el número de Libros escritos en el mes: "))


    def bono(self):
        if self.nroLibros > 40:
            print(f"{self.nombres}, usted recibirá este mes su bono")
        else:
            print(f"{self.nombres}, este mes usted no aplica al bono.")


def controlador(objeto):
    objeto.datos()
    objeto.bono()


objeto1 = Editor()
controlador(objeto1)

objeto2 = Escritor()
controlador(objeto2)
"""

# PROBLEMA 03:
# Elaborar una LI, en la cual se tenga dos clases, una clase EmpleadoFullTime, y otra EmpleadoPartTime, 
# dichas clases debe de contar con un método llamado bono, el cual retorne como bono el 30% del sueldo,
# dicho bono deberá ser utilizado para la clase empleadoPartTime gracias a que hereda de la clase EmpleadoFullTime
# NOTA: trabajar y aprobechar toda la herencia.

class EmpleadoFullTime:
    def __init__(self, nombre, cargo, horas, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.horas = horas
        self.sueldo = sueldo

    def bono(self):
        return (self.sueldo * 0.3)

class EmpleadoPartTime(EmpleadoFullTime):
    def __init__(self, nombre, cargo, horas, sueldo):
        super().__init__(nombre, cargo, horas, sueldo)


def controlador(objeto):
    cantidad_bono = objeto.bonoFamiliar()
    print(f"{objeto.nombre}, su bono respectico es de {cantidad_bono}")


empleado_1 = EmpleadoFullTime("Andrea", "Analista", 160, 2000)
controlador(empleado_1)

empleado_2 = EmpleadoPartTime("Luis", "Developer", 180, 2500)
controlador(empleado_2)
