def cargarArticulo():
    articulos = []
    for i in range(5):
        print(f"Artículo {i+1}")
        nombre = input(f"Ingrese el nombre : ")
        precio = float(input(f"Ingrese el precio : "))
        articulos.append((nombre, precio))
    return articulos

def imprimirArticulos(articulos):
    print("Artículos y precios:")
    for articulo in articulos:
        print(f"{articulo[0]}: {articulo[1]:.2f}")

def imprimirMayor(articulos):
    articuloMayor = articulos[0]
    for articulo in articulos:
        if articulo[1] > articuloMayor[1]:
            articuloMayor = articulo
    print(f"El artículo más caro es:\n\t{articuloMayor[0]}: S/ {articuloMayor[1]:.2f}")

def imprimirMenor(importe, articulos):
    print(f"Artículos con precio menor o igual a  S/{importe:.2f}:")
    for articulo in articulos:
        if articulo[1] <= importe:
            print(f"{articulo[0]}:  S/{articulo[1]:.2f}")


try:
    articulos = cargarArticulo()
    imprimirArticulos(articulos)
    imprimirMayor(articulos)
    importe = float(input("Ingrese un importe para buscar artículos con precio menor o igual: "))
    imprimirMenor(importe, articulos)
except ValueError:
    print("Por favor, ingrese un número válido.")