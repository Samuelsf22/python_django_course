import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123',
        database='tienda'
    )

    if conexion.is_connected():
        cursor = conexion.cursor()

        queryInsert = "INSERT INTO clientes (nombre, apellido, edad, dni) VALUES (%s, %s, %s, %s)"
        datos = [
            ("Juan", "Perez", 30, "12345678"),
            ("Maria", "Gomez", 25, "23456789"),
            ("Pedro", "Lopez", 40, "34567890"),
            ("Ana", "Martinez", 28, "45678901"),
            ("Luis", "Rodriguez", 35, "56789012"),
            ("Laura", "Diaz", 27, "67890123"),
            ("Carlos", "Sanchez", 32, "78901234"),
            ("Sofia", "Gonzalez", 22, "89012345"),
            ("Daniel", "Torres", 29, "90123456")
        ]
        cursor.executemany(queryInsert, datos)
        conexion.commit()

        querySelect = "SELECT * FROM clientes"
        cursor.execute(querySelect)
        clientes = cursor.fetchall()
        print("Todos los registros de la tabla 'clientes':")
        for cliente in clientes:
            print(cliente)

        querySelectOne = "SELECT * FROM clientes WHERE dni = %s"
        value = ('34567890',)
        cursor.execute(querySelectOne, value)
        clienteSelect = cursor.fetchone()

        print("\nUn registro de la tabla 'clientes' (filtrado por DNI):")
        print(clienteSelect)

        queryDelete = "DELETE FROM clientes WHERE dni = %s"
        value = ('78901234',)
        cursor.execute(queryDelete, value)
        conexion.commit()
        print("\nSe ha eliminado un registro de la tabla 'clientes'.")

        queryAlter = "ALTER TABLE clientes ADD COLUMN tipo_de_sangre VARCHAR(10)"
        cursor.execute(queryAlter)
        conexion.commit()
        print("\nLa estructura de la tabla 'clientes' se ha alterado para agregar 'tipo_de_sangre'.")

except Error as ex:
    print(f"Hubo un error en las operaciones con la base de datos:\n{ex}")