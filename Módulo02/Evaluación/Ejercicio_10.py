class Persona:
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni


class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, dni, sueldo):
        super().__init__(nombre, apellido, edad, dni)
        self.sueldo = sueldo
        self.bonoFamiliar = self.sueldo * 0.07

    def sueldoTotal(self):
        return self.sueldo + self.bonoFamiliar

try:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))

    while True:
        dni = input("Ingrese el DNI (8 dígitos exactos): ")
        if len(dni) == 8 and dni.isdigit():
            break
        print("El DNI debe tener exactamente 8 dígitos numéricos.")

    while True:
        sueldo = float(input("Ingrese el sueldo: "))
        if sueldo > 0:
            break
        print("El sueldo debe ser un número positivo.")

    trabajador = Trabajador(nombre, apellido, edad, dni, sueldo)

    print("\nDatos del trabajador:")
    print(f"Nombre: {trabajador.nombre}")
    print(f"Apellido: {trabajador.apellido}")
    print(f"Edad: {trabajador.edad}")
    print(f"DNI: {trabajador.dni}")
    print(f"Sueldo: {trabajador.sueldo}")
    print(f"Bono Familiar: {trabajador.bonoFamiliar:.2f}")
    print(f"Total a recibir: {trabajador.sueldoTotal():.2f}")

except ValueError:
    print("Asegúrate de ingresar valores válidos.")
