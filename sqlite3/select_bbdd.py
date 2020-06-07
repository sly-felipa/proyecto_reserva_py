import sqlite3

# establacer conexión
conexion = sqlite3.connect("proyecto_reserva/sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
consulta = conexion.cursor()

# sql = "select * from test"

# if consulta.execute(sql):
#     filas = consulta.fetchall()
#     for f in filas:
#         print(f[0],f[1],f[2],f[3],f[4])

sql = "select * from test where id=%s" % 1
consulta.execute(sql)
fila = consulta.fetchone()
print("consulta: ", fila[0], fila[1], fila[2], fila[3], fila[4] )
consulta.close()
conexion.commit()
conexion.close()