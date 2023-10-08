class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrarPantalla(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"



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
    print(punto.cuadrante())
except ValueError:
    print("Por favor ingrese valores numéricos válidos.")