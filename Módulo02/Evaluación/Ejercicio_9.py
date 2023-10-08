class Persona:
    def __init__(self, nombre, apellido, edad, dni, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.altura = altura
        self.peso = peso

    def imprimir(self):
        print(f"\tNombre: {self.nombre}")
        print(f"\tApellido: {self.apellido}")
        print(f"\tEdad: {self.edad}")
        print(f"\tDNI: {self.dni}")
        print(f"\tAltura: {self.altura} m")
        print(f"\tPeso: {self.peso} kg")

    def resultado(self):
        return self.peso / (self.altura ** 2)


try:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))

    while True:
        dni = input("Ingrese el DNI: ")
        if len(dni) == 8 and dni.isdigit():
            break
        print("El DNI debe tener exactamente 8 dígitos numéricos.")


    while True:
        altura = float(input("Ingrese la altura (hasta 2.5 m): "))
        if 0 < altura <= 2.5:
            break
        print("La altura debe estar entre 0 y 2.5 metros.")

    peso = float(input("Ingrese el peso (en kg): "))

    persona = Persona(nombre, apellido, edad, dni, altura, peso)

    print("\nDatos ingresados:")
    persona.imprimir()
    print(f"El índice de masa corporal (IMC) es: {persona.resultado():.2f}")
except ValueError:
    print("Asegúrate de ingresar valores válidos.")