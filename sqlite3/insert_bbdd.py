import sqlite3, datetime

# establacer conexión
conexion = sqlite3.connect("proyecto_reserva/sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
consulta = conexion.cursor()

# tomar valores para la columna - tupla
# argumentos = (id, cadena, entero, decimal, datetime.date.today()) # 2020-12-30

# insert
sqlUsuario = """
INSERT INTO usuario (nombre_usuario, nombre, apellido, contraseña, registro, email ) 
VALUES ('1','Fulanito','Perez', '12345', '01/02/2020','fulanito@mail.com'), 
('2','Venganito','Bottini','venga2020','05/02/2020','venganito@mail.com'),
('9','user','Uprueba','12345','10/02/2020','fulanito@mail.com');
"""

sqlHotel = """
INSERT INTO hotel (codigo_hotel, nombre, categoria, cantidad_habitaciones) 
VALUES ('h1','Perico','4',3),
('h2','Dorada','3',2),
('h3','Salmón','1',3),
('h9','Hprueba','3',2);
"""

sqlHabitacion = """
INSERT INTO habitacion (codigo_habitacion,codigo_hotel, tipo_habitacion, capacidad, precio,reservado)
VALUES ('p1','h1','simple',2,10,0),
('p2','h1','doble',1,15,0),
('p3','h1','simple',3,8,0),
('d1','h2','simple',4,5,0),
('d2','h2','simple',2,8,0),
('s1','h3','doble',2,8,0),
('s2','h3','doble',2,10,0),
('s3','h3','simple',2,10,0),
('pr1','h9','doble',1,10,1),
('pr2','h9','simple',2,10,0);
"""

sqlReserva = """
INSERT INTO reserva (codigo_habitacion,nombre_usuario,fecha_reserva,checking,checkout)
VALUES ('pr1','9','11/05/2020','11/05/2020','15/05/2020'); 
"""
sqlServicios = """
INSERT INTO servicios (codigo_habitacion, climatizacion, minibar, descripcion)
VALUES ('p1','0','1','Es bonito'),
('p2','0','1','Es amplia y tiene una buena vista.'),
('p3','0','0','Es bonito'),
('d1','0','1',''),
('d2','1','1','Es bonito'),
('s1','0','0','Es bonito'),
('s2','1','1','Es bonito'),
('s3','0','0','Es bonito'),
('pr1','0','0','Es prueba'),
('pr2','0','1','');
"""
# os.getcwd()

# ejecutar insert
if consulta.execute(sqlUsuario): 
    print("sqlUsuario correcto")
else:
    print("sqlUsuario INcorrecto")

if (consulta.execute(sqlHotel)): 
    print("sqlHotel correcto")
else:
    print("sqlHotel INcorrecto")

if (consulta.execute(sqlHabitacion)): 
    print("sqlHabitacion correcto")
else:
    print("sqlHabitacion INcorrecto")
   
if (consulta.execute(sqlReserva)): 
    print("sqlReserva correcto")
else:
    print("sqlReserva INcorrecto")
    
if (consulta.execute(sqlServicios)): 
    print("sqlServicios correcto")
else:
    print("sqlServicios INcorrecto")

# termina la consulta
consulta.close()

# guardar datos en bbdd
conexion.commit()

# cerrar conexión
conexion.close()

