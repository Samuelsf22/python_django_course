# DELETE: eliminar registros, tablas, base de datos.

import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexion es segura")

mycursor = conexion.cursor()
query = "DELETE FROM clientes WHERE nombre = 'Carlos'"
mycursor.execute(query)
conexion.commit()
print(f"{mycursor.rowcount}, registros eliminado(s)")

# PREVENCION DEL INJECT SQL
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexion es segura")

mycursor = conexion.cursor()
query = "DELETE FROM clientes WHERE direccion = %s"
value =("Jr. Prado 133",)
mycursor.execute(query)
conexion.commit()
print(f"{mycursor.rowcount}, registros eliminado(s)")

# ELIMINACIÓN DE TABLAS
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexion es segura")

mycursor = conexion.cursor()
query = "DROP TABLE donadores;"
value =("Jr. Prado 133",)
mycursor.execute(query)
conexion.commit()