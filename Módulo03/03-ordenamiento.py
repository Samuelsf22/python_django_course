# ORDENAMIENTO EN LA MISMA CONSULTA DE BASE DE DATOS
# ORDER BY --> ORDEN DE FORMA ASCENDENTE (prederteminada)
# DESC --> ORDENAMIENTO DE FORMA DESCENDENTE

# 16 ORDENAMIENTO DE FORMA DESCENDENTE
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

query = 'SELECT * FROM clientes ORDER BY nombre DESC'
mycursor.execute(query)
resultado = mycursor.fetchall()
for x in resultado:
    print(x)
