class Estudiante:
    def __init__(self, nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas

    def imprimir(self):
        print(f"Nombre completo : {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        for i in range(len(notas)):
            print(f"\tNota {i+1}: {notas[i]}")

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def verificarPromovido(self):
        promedio = self.promedio()
        if promedio >= 13:
            return f"Promovido con una nota de {promedio:.2f}"
        else:
            return f"No promovido, con una nota de {promedio:.2f}"


try:
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))

    notas = []
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe en un rango de 0 y 20. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor ingrese valores numéricos válidos.")

    estudiante = Estudiante(nombre, apellido, edad, notas)
    estudiante.imprimir()
    promovido = estudiante.verificarPromovido()
    print(f"Resultado: {promovido}")

except ValueError:
    print("Asegúrate de ingresar valores válidos.")
