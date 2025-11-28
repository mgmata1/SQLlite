
import sqlite3
conn = sqlite3.connect()
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXIST parques
    id INTEGRER, primary key, nombre VACHART (50))

)

conn.close() 

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, ciudad, id, direccion, caracteristica

nombre = "parque Lineal 1"
ciudad = "Loja"
id = "1011019091"
direccion = Av. Limones
caracteristica = urbano
cadena_sql = """INSERT INTO Autor (nombre, ciudad, id, direccion, caracteristica) \
VALUES ('%s', '%s', '%s', %d , %s);""" % (nombre, ciudad, id, direccion, caracteristica)

# ejecutar el SQL
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()


# ejecutar el SQL
cursor.execute(cadena_sql)

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, ciudad, id, direccion, caracteristica
nombre = "Parque Redondel"
ciudad = "Manta"
id = "10110190933
direccion = Via del Sol
caracteristica = recreativo
cadena_sql = """INSERT INTO Autor (nombre, ciudad, id, direccion, caracteristica) \
VALUES ('%s', '%s', '%s', %d, %s);""" % (nombre, ciudad, id, direccion, caracteristica)

# ejecutar el SQL
cursor.execute(cadena_sql)

# nuevo registo
nombre = "Parque Botanico"
ciudad = "Quito"
id = "10110190123
direccion = Av. Los Rosales
caracteristica = rural
cadena_sql = """INSERT INTO Autor (nombre, ciudad, id, direccion, caracteristica) \
VALUES ('%s', '%s', '%s', %d, %s);""" % (nombre, ciudad, id, direccion, caracteristica)

cursor.execute(cadena_sql)

# nuevo registo
nombre = "Parque Municipal"
ciudad = "Guayaquil"
id = "10110190567
direccion = Malecon 2000
caracteristica = ruralrecreativo
cadena_sql = """INSERT INTO Autor (nombre, ciudad, id, direccion, caracteristica) \
VALUES ('%s', '%s', '%s', %d, %s);""" % (nombre, ciudad, id, direccion, caracteristica)


cursor.execute(cadena_sql)

# inicio proceso de elminación
cadena = """DELETE from Autor WHERE nombre='%s'""" % ("Parque Municipal")
cursor.execute(cadena)
conn.commit()


# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# ejecutar el SQL
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()

