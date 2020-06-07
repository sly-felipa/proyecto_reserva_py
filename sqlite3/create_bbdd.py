# importamos la librería
import sqlite3

# hacemos la conexión con la bbdd
conexion = sqlite3.connect("proyecto_reserva/sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
consulta = conexion.cursor()

sqlUsuario = """
CREATE TABLE usuario(
nombre_usuario VARCHAR2(20) PRIMARY KEY,
nombre VARCHAR2(20),
apellido VARCHAR2(20),
contraseña VARCHAR2(20),
registro DATE,
email VARCHAR2(30));"""

sqlHotel = """
CREATE TABLE hotel(
codigo_hotel VARCHAR2(20) PRIMARY KEY,
nombre VARCHAR2(15),
categoria NUMBER(1),
cantidad_habitaciones NUMBER(2));"""

sqlHabitacion = """
CREATE TABLE habitacion(
codigo_habitacion VARCHAR2(5) PRIMARY KEY,
codigo_hotel VARCHAR2(20),
tipo_habitacion VARCHAR2(20),
capacidad NUMBER(2),
precio NUMBER(3),
reservado NUMBER(1),
CONSTRAINT fk_codigo_hotel FOREIGN KEY (codigo_hotel) REFERENCES HOTEL (codigo_hotel));"""

sqlReserva = """
CREATE TABLE reserva(
codigo_habitacion VARCHAR2(10),
nombre_usuario VARCHAR2(20),
fecha_reserva DATE,
checking DATE,
checkout DATE,
CONSTRAINT pk_reserva PRIMARY KEY (codigo_habitacion, nombre_usuario, fecha_reserva),
CONSTRAINT fk_codigo_habitacion FOREIGN KEY (codigo_habitacion) REFERENCES HABITACION(codigo_habitacion),
CONSTRAINT fk_nombre_usuario FOREIGN KEY (nombre_usuario) REFERENCES USUARIO(nombre_usuario));"""

sqlServicios = """
CREATE TABLE servicios(
codigo_habitacion VARCHAR2(5) PRIMARY KEY,
climatizacion NUMBER(1),
minibar NUMBER(1),
descripcion VARCHAR2(40),
CONSTRAINT fk_servicios FOREIGN KEY (codigo_habitacion) REFERENCES HABITACION(codigo_habitacion));
"""


# ejecutar consulta
if (consulta.execute(sqlUsuario)): print("tabla 1")
else: print("tabla NO creada 1")

if (consulta.execute(sqlHotel)): print("tabla 2")
else: print("tabla NO creada 2")

if (consulta.execute(sqlHabitacion)): print("tabla 3")
else: print("tabla NO creada 3")

if (consulta.execute(sqlReserva)): print("tabla 4")
else: print("tabla NO creada 4")

if (consulta.execute(sqlServicios)): print("tabla 5")
else: print("tabla NO creada 5")

# terminamos la consulta
consulta.close()

# guardamos los cambios en la bbdd
conexion.commit()

# cerramos la conexión a la bbdd
conexion.close()