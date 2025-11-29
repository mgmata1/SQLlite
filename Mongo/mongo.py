"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import parques

# se obtiene la colección general (base de datos)

db = parques.ejemploMongo001
coleccion = db.autores

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Parque Lineal", "ciudad": "Loja",
"Caracteristica":"rural", "id_parque": 100, "direccion": "Av. Limones"}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Parque Lineal 2", "Ciudad": "Manta", "caracteristica":"recreativo",
"id_parque": 90, "direccion": " Av. Los Ceibos"}
{"nombre": "Parque Lineal 3", "Ciudad": "Guayaquil", "caracteristica":"municipal",
"id_parque": 80, "direccion": " Av. Los Almendros"}
]

coleccion.insert_many(lista)


"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import parques

# se obtiene la colección general (base de datos)

db = parques.ejemploMongo001
coleccion = db.autores

# se usa método find_one, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one()
print(data_01)

# se usa método find, a partir de la colección
print("Muestra todos los documentos de la base de datos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = parques.ejemploMongo001
coleccion = db.autores

# se usa método find_one con parámetros, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one({'nombre':'Parque Lineal 2'})
print(data_01)

# se usa método find con parámetros, a partir de la colección
print("Muestra todos los documentos de la base de datos que cumplan con la \
condición")
data_02 = coleccion.find({'numero_publicaciones':{"$lt":100}})
for registro in data_02:
    print(registro)

    """
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import parques

# se obtiene la colección general (base de datos)

db = parques.ejemploMongo001
coleccion = db.autores

print("Muestra todos los documentos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

# se usa método delete_many con parámetros, a partir de la colección
# para eliminar un documento de la colección
print("Proceso para borrar un documento de una colección")
coleccion.delete_many({'numero_publicaciones':80})

print("Muestra todos los documentos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

    """
    Agregar información en una colección de MongoDB
    desde Python
"""
from pymongo import MongoParques
parques = MongoParques('mongodb://localhost:27010/')