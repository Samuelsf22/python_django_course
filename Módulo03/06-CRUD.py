# C-reate    Insert
# R-ead      Select
# U-pdate    Update
# D-elete    Drop


# Crear nuestra tabla Usuario dentro de la DB Servicios
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
    mycursor.execute("CREATE TABLE usuario (nombre varchar(255), direccion varchar(255), celular varchar(15));")
else:
    print("Hubo un error en la conexión de BD")
    

# 02 Realización del CRUD
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='servicios',
    port='3306'
)

# CREACIÓN DEL CURSOR EL CUAL SE TRABAJA EN DIFERENTES PARTES DEL CÓDIGO
mycursor = conn.cursor()


def menuPrincipal():
    continuar = True
    while continuar:
        print("*****MENÚ PRINCIPAL*****")
        print("\t1. Ver Usuarios")
        print("\t2. Ingresar Usuario")
        print("\t3. Actualizar Usuario")
        print("\t4. Eliminar Usuario")
        print("\t5. Salir")
        opcion = int(input("Selecciona una opción : "))

        if opcion < 1 or opcion > 5:
            print(f"""\nLa opción {opcion} es incorrecta,
                     Intente de nuevo:\n""")
        elif opcion == 5:
            continuar = False
            print("Gracias por utilizar el programa")
            break
        else:
            # Llamar a una función en la cual envía la opción
            ejecutarOpcion(opcion, mycursor)


def verUsuarios(mycursor):
    mycursor.execute("SELECT * FROM usuarios;")
    resultado = mycursor.fetchall()
    for x in resultado:
        print(x)


def anadirUsuario(mycursor):
    codigo = int(input("Ingrese un código de usuario: "))
    nombres = input("Ingrese sus nombres: ")
    celular = input("Ingrese su número de celular: ")
    query = "INSERT INTO usuarios (codigo, nombre, celular) VALUES (%s, %s, %s);"
    values = (codigo, nombres, celular)
    mycursor.execute(query, values)
    conn.commit()
    print(f"{mycursor.rowcount} Resgistro realizado.")
    print("Usuario registrado")


def actualizarUsuario(mycursor):
    codigo = int(input("Ingrese un código a actualizar: "))
    nombres = input("Ingrese sus nombres: ")
    celular = input("Ingrese su número de celular: ")
    query = "UPDATE usuarios SET nombre = %s, celular = %s WHERE codigo = %s;"
    values = (nombres, celular, codigo)
    mycursor.execute(query, values)
    conn.commit()
    print("Usuario actualizado")


def eliminarUsuario(mycursor):
    codigo = int(input("Ingrese un código para eliminar: "))
    query = "DELETE FROM usuarios WHERE codigo = %s;"
    values = (codigo, )
    mycursor.execute(query, values)
    conn.commit()
    print("Usuario actualizado")


def ejecutarOpcion(opcion, mycursor):
    if opcion == 1:
        verUsuarios(mycursor)
    if opcion == 2:
        anadirUsuario(mycursor)
    if opcion == 3:
        actualizarUsuario(mycursor)
    if opcion == 4:
        eliminarUsuario(mycursor)


menuPrincipal()
