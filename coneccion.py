
import sqlite3

conn = sqlite3.connect()

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXIST parques
    id INTEGRER, primary key, nombre VACHART (50))

)

conn.close() 

nombre = "parque 1"
ubicacion = "ceibos"
id = "1011019091"
caracteristica = rural
cadena_sql = """INSERT INTO Autor (nombre, ubicacion, id, caracteristica) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, ubicacion, id, cracteristica)

# ejecutar el SQL
cursor.execute(cadena_sql)
