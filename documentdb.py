import pymongo
from pymongo.errors import ConnectionFailure, DuplicateKeyError
import sys
import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from configparser import ConfigParser


parser = ConfigParser(interpolation=None)
parser.read('dwh.cfg')

ddb_url = parser.get('documentdb','url')
ddb_user = parser.get('documentdb','user')
ddb_pass = parser.get('documentdb','password')

#Validar si trae correctamente las variables
print(ddb_url)
print(ddb_user)
print(ddb_pass)

##########################################################################################


##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb://{}:{}@{}:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem'.format(ddb_user,ddb_pass,ddb_url)) 


##Specify the database to be used
db = client.HYMDb
db = client['HYMDb']

##Specify the collection to be usede
col = db.Consultants
col = db['Consultants']

##Insert a single document 
collection.insert_one({'hello':'Amazon DocumentDB'}) # Automaticamente le agrega un ID mongo si no tiene
collection.insert_one({'_id':2, 'name':'keybord', 'price':300}) # Agregandole un id, siempre se escribe con "_id"

##Insertar varios documentos a la collections
product_one = ['name':'mouse']
product_two = {'name':'monitor'}

collection.insert_many([product_one,product_two])

# Buscar todos los valores de un documento
results = collection.find()
for r in results:
    print( r['name'] )

# Buscar por valor
results = collection.find({"name":"mouse"})
for r in results:
    print( r )

# Buscar valor por coincidencia
results = collection.find({"name":"/mouse/"})
for r in results:
    print( r )


##Buscar 1 solo dato con find_one
x = col.find_one({'CodPais':'MX'})

for i in x.keys():
    print(i, ' : ' , x[i])

##Print the result to the screen
print(x)

# Eliminar un documento, si hay varios, elimina el primero que encuentre
collection.delete_one({"price":300})

# Eliminar varios documentos
collection.delete_many({"price":300})

# Eliminar todos los datos de la collection
collection.delete_many({})

# Actualizar 1 dato
collection.update_one({"name":"laptop"}, {"$set": {"name":"Keyboard", "price": 300} })

# Actualizar 1 dato, pero incluir un campo mas
collection.update_one({"name":"laptop"}, {"$inc": {"price": 300} })

# Actualizar varios
collection.update_many({"name":"laptop"}, {"$set": {"name":"Keyboard", "price": 300} })
collection.update_many({"name":"laptop"}, {"$inc": {"price": 300} })

#Contar datos en una collection
number_of_collection = collection.count_documents({})
print( number_of_collection )

##Close the connection
client.close()


"""

show databases

show collections

use teststore

db.products.find()


"""
