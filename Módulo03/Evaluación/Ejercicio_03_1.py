import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='tienda',
        port='3306'
    )

    if conexion.is_connected():
        print("La conexión fue exitosa")
        cursor = conexion.cursor()
        datos = [
            ("Televisión", 1000, 10),
            ("Cocina", 500, 5),
            ("Lavadora", 2000, 20),
            ("Nevera", 1500, 15)
        ]

        queryInsert = f"INSERT INTO productos (descripcion, precio, descuento) VALUES (%s, %s, %s)"
        cursor.executemany(queryInsert, datos)
        querySelect = "SELECT * FROM productos"
        cursor.execute(querySelect)
        productos = cursor.fetchall()
        print("Todos los registros de la tabla 'productos':")

        for producto in productos:
            print(producto)

        querySelect2 = "SELECT * FROM productos WHERE id = 2"
        cursor.execute(querySelect2)
        producto2 = cursor.fetchone()

        print("\nEl segundo registro de la tabla 'productos':")
        print(producto2)

        queryDelete = "DELETE FROM productos WHERE id = 4"
        cursor.execute(queryDelete)
        conexion.commit()
        print("Se elimino el producto con id = 4")
        queryAlter = "ALTER TABLE productos ADD COLUMN marca VARCHAR(255) NOT NULL"
        cursor.execute(queryAlter)
        conexion.commit()
        print("Las operaciones se han realizado correctamente.")

except Error as ex:
    print(f"Hubo un error en la conexión o creación de la base de datos")
