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

        queryDB = 'CREATE DATABASE IF NOT EXISTS colegio'
        cursor.execute(queryDB)

        queryUse = 'USE colegio'
        cursor.execute(queryUse)

        queryTable = '''
            CREATE TABLE IF NOT EXISTS estudiante (
                codigo INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                edad INT NOT NULL,
                grado VARCHAR(255) NOT NULL
            )
        '''
        cursor.execute(queryTable)

        print("La base de datos 'colegio' y la tabla 'Estudiante' se han creado exitosamente.")

except Error as ex:
    print(f"Hubo un error en la conexión o creación de la base de datos:\n{ex}")