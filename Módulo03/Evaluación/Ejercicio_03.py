import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123'
    )

    if conexion.is_connected():
        print("La conexión fue exitosa")

        cursor = conexion.cursor()

        queryDB = 'CREATE DATABASE IF NOT EXISTS tienda'
        cursor.execute(queryDB)

        queryUse = 'USE tienda'
        cursor.execute(queryUse)

        queryTableProductos = '''
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descripcion TEXT NOT NULL,
                precio DECIMAL(10,2) NOT NULL,
                descuento DECIMAL(10,2) NOT NULL                
            )
        '''
        cursor.execute(queryTableProductos)

        queryTableClientes = '''
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                edad INT (3) NOT NULL,
                dni VARCHAR(8) NOT NULL
            )
        '''
        cursor.execute(queryTableClientes)

        print("La base de datos 'tienda' y las tablas 'productos' y 'clientes' se han creado exitosamente.")

except Error as ex:
    print(f"Hubo un error en la conexión o creación de la base de datos:\n{ex}")