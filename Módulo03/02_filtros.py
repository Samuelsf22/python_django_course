# FILTRO CON UN CAMPO
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

query = "SELECT * FROM clientes WHERE nombre  = 'Fiorella';"
mycursor.execute(query)
resultado = mycursor.fetchall()
for x in resultado:
    print(x)

query = "SELECT * FROM clientes WHERE direccion  = 'Jr. Prado 123';"
mycursor.execute(query)
resultado = mycursor.fetchall()
for x in resultado:
    print(x)

query = "SELECT * FROM clientes WHERE id  = '17';"
mycursor.execute(query)
resultado = mycursor.fetchall()
for x in resultado:
    print(x)


# INJECT SQL - prevención
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

query = 'SELECT * FROM clientes WHERE direccion = %s'
value = ("Jr. Lima 123", )
mycursor.execute(query, value)

resultado = mycursor.fetchall()
for x in resultado:
    print(x)