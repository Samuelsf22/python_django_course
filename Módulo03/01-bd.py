import mysql.connector # me permite trabajar con mi paquete conector.
from mysql.connector import Error # Nos permite mostrar un mensaje de error relacionado a base de datos

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = 'password',
        db = 'world'
    )
    if conexion.is_connected():
        print("La conexion fue exitosa")
except Error as ex:
    print(f"Hubo un error en la conexion:\n{ex}")




# 1     CONEXIÓN SIMPLE
import mysql.connector
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
)

if conexion.is_connected():
    print("La conexion fue exitosa")


# 2     CREACIÓN DE BASE DE DATOS
import mysql.connector
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password'
)

mycursor = conexion.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS servicios")

# 3     VERIFICACIÓN DE BASE DE DATOS
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password'
)

mycursor = mysql.cursor()
mycursor.execute("SHOW DATABASES;")

for x in mycursor:
    print(x)

# 4     CONEXIÓN SIPLE
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexión es correcta.")


# 5     CREACIÓN DE UNA TABLA EN LA BASE DE DATOS
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexión es correcta.")

mycursor = conexion.cursor()
mycursor.execute("CREATE TABLE clientes(nombre varchar(255), direccion varchar(255), celular varchar(15));")

#6      VERIFICAR LA TABLA EN UNA BASE DE DATOS
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexión es correcta.")

mycursor = conexion.cursor()
mycursor.execute("SHOW TABLES;")

for x in mycursor:
    print(x)

# EJERCICIO PARA PUNTOS
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)

if conexion.is_connected():
    print("La conexión es correcta.")

mycursor = conexion.cursor()
mycursor.execute("CREATE TABLE Usuario (id_cliente INT, nombre VARCHAR(100),direccion VARCHAR(200));")
mycursor.execute("CREATE TABLE Pedidos (id_pedido INT,fecha_pedido DATE,total DECIMAL(10, 2));")
mycursor.execute("CREATE TABLE Productos (id_producto INT,nombre_producto VARCHAR(150),precio DECIMAL(10, 2));")
mycursor.execute("CREATE TABLE Empleados (id_empleado INT,nombre_empleado VARCHAR(100),cargo VARCHAR(50));")

mycursor.execute("SHOW TABLES;")

for x in mycursor:
    print(x)

#7 
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)
if conexion.is_connected():
    print("Conexión segura")
    mycursor = conexion.cursor()
    mycursor.execute("CREATE TABLE donadores (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), direccion VARCHAR(255));")
    print("La creación de la tabla fue exitosa")
else:
    print("Hubo un error en la conexión")

#8 AÑADIR PK A UNA TABLA EXISTENTE
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'servicios',
    port = '3306'
)
if conexion.is_connected():
    print("Conexión segura")
    mycursor = conexion.cursor()
    mycursor.execute("ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")
    print("Se añadio el PK a la tabla.")
else:
    print("Hubo un error en la conexión")

# 9 INGRESAR DATOS A UNA TABLA bd EN ESPECÍFICO
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
query = "INSERT INTO clientes(nombre, direccion, celular) VALUES (%s, %s, %s)"
value = ("Carlos", "Jr. Lima nro.123", "987456321")

mycursor.execute(query, value)
conexion.commit() # ES un método que guarda los cambios realizados

print(mycursor.rowcount, "Registro realizado")

#10     INGRESO DE REGISTRO MULTIPLES
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

query = "INSERT INTO clientes(nombre, direccion, celular) VALUES (%s, %s, %s)"
values = [
    ('Luis', 'Jr. Lima 123', '987456321'),
    ('Miguel', 'Jr. Prado 123', '963258741'),
    ('Andra', 'Av. Proceres 123', '985741236'),
    ('Fiorella', 'Av. Calixto 123', '958674123'),
    ('Alisson', 'Calle Real 125', '912457863')
]
mycursor.executemany(query, values)
conexion.commit()
print(f"{mycursor.rowcount}, Registro Realizados")


#11 MOSTRAR DATOS DE UNA TABLA EN CONCRETO
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
mycursor.execute("SELECT * FROM clientes;")
# Obtenemos el resultado de la consulta
resultado = mycursor.fetchall()

for x in resultado:
    print(x)

# 12 MOSTRAR EL PRIMER REGISTRO DE UNA CONSULTA
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
mycursor.execute("SELECT * FROM clientes;")

resultado = mycursor.fetchone()
print(resultado)