class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrarPantalla(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")


try:
    x = input("Ingrese la coordenada X del punto (default 0): ")
    y = input("Ingrese la coordenada Y del punto (default 0): ")

    if x == "":
        x = 0
    else:
        x = float(x)

    if y == "":
        y = 0
    else:
        y = float(y)

    punto = Punto(x, y)
    punto.mostrarPantalla()
except ValueError:
    print("Por favor ingrese valores numéricos válidos.")