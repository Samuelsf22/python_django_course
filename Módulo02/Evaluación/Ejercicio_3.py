class Punto:

    def imprimir(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")


try:
    punto = Punto()
    punto.x = float(input("Ingrese la coordenada X del punto: "))
    punto.y = float(input("Ingrese la coordenada Y del punto: "))
    punto.imprimir()

except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para las coordenadas.")