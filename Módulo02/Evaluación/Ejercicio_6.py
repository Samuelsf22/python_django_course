class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrarPantalla(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def vector(self, puntoFinal):
        vector_x = puntoFinal.x - self.x
        vector_y = puntoFinal.y - self.y
        return Punto(vector_x, vector_y)

    def distancia(self, puntoFinal):
        distancia = ((puntoFinal.x - self.x) ** 2 + (puntoFinal.y - self.y) ** 2) ** 0.5
        return distancia


try:
    x1 = input("Ingrese la coordenada X del punto inicial (default 0): ")
    x1 = float(x1) if x1 != "" else 0

    y1 = input("Ingrese la coordenada Y del punto inicial (default 0): ")
    y1 = float(y1) if y1 != "" else 0

    x2 = input("Ingrese la coordenada X del punto extremo (default 0): ")
    x2 = float(x2) if x2 != "" else 0

    y2 = input("Ingrese la coordenada Y del punto extremo (default 0): ")
    y2 = float(y2) if y2 != "" else 0

    puntoInicio = Punto(x1, y1)
    puntoFinal = Punto(x2, y2)

    vectorResultante = puntoInicio.vector(puntoFinal)
    distanciaPuntos = puntoInicio.distancia(puntoFinal)

    print("Vector resultante:")
    vectorResultante.mostrarPantalla()

    print(f"Distancia entre los puntos: {distanciaPuntos:.2f}")

except ValueError:
    print("Por favor ingrese valores numéricos válidos.")
