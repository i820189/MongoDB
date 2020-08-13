# MongoDB - Tools

Estos son algunos comandos que ayudan a manejar los datos desde una base de datos no relacional MongoDB, también sirve para manipular data en DocumentDB(AWS) que trabaja sobre la misma tecnología de MOngoDB

## Imports
```python
import pymongo
from pymongo.errors import ConnectionFailure, DuplicateKeyError
```

## Specify the database to be used
```python
db = client.HYMDb
db = client['HYMDb']
```

## Specify the collection to be usede
```python
col = db.Consultants
col = db['Consultants']
```

## Insert a single document 
```python
collection.insert_one({'hello':'Amazon DocumentDB'}) 
```

## Automaticamente le agrega un ID mongo si no tiene
```python
collection.insert_one({'_id':2, 'name':'keybord', 'price':300}) # Agregandole un id, siempre se escribe con "_id"
```

## Insertar varios documentos a la collections
```python
product_one = ['name':'mouse']
product_two = {'name':'monitor'}

collection.insert_many([product_one,product_two])
```

## Buscar todos los valores de un documento
```python
results = collection.find()
for r in results:
    print( r['name'] )
```

## Buscar por valor
```python
results = collection.find({"name":"mouse"})
for r in results:
    print( r )
```

## Buscar valor por coincidencia
```python
results = collection.find({"name":"/mouse/"})
for r in results:
    print( r )
```

## Buscar 1 solo dato con find_one
```python
x = col.find_one({'CodPais':'MX'})

for i in x.keys():
    print(i, ' : ' , x[i])
```

## Print the result to the screen
```python
print(x)
```

## Eliminar un documento, si hay varios, elimina el primero que encuentre
```python
collection.delete_one({"price":300})
```

## Eliminar varios documentos
```python
collection.delete_many({"price":300})
```

## Eliminar todos los datos de la collection
```python
collection.delete_many({})
```

## Actualizar 1 dato
```python
collection.update_one({"name":"laptop"}, {"$set": {"name":"Keyboard", "price": 300} })
```

## Actualizar 1 dato, pero incluir un campo mas
```python
collection.update_one({"name":"laptop"}, {"$inc": {"price": 300} })
```

## Actualizar varios
```python
collection.update_many({"name":"laptop"}, {"$set": {"name":"Keyboard", "price": 300} })
collection.update_many({"name":"laptop"}, {"$inc": {"price": 300} })
```

## Contar datos en una collection
```python
number_of_collection = collection.count_documents({})
print( number_of_collection )
```

## Close the connection
```python
client.close()
```