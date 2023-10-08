# ACTUALIZACIÓN
# Se actualiza mediante el comando UPDATE

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
query = "UPDATE clientes SET nombre = 'Carla' WHERE nombre = 'Luis';"
mycursor.execute(query)
conexion.commit()
