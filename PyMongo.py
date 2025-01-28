import pymongo
#Importar con: "python -m pip install pymongo" en el cmd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Creación de la base de datos
mydb = myclient["Ejercicio"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "Ejercicio" in dblist:
  print("La base de datos existe")

mycol = mydb["Ejercicio"]

collist = mydb.list_collection_names()
if "Ejercicio" in collist:
  print("The collection exists.")

#Insertar  
def insertarEjercicio(nombre,dificultad):
  mydict = { "nombre": nombre, "dificultad": dificultad }
  mycol.insert_one(mydict)

#Update
def updateNombreEjercicio(nombre,nuevoNombre):
  myquery = { "nombre": nombre }
  newvalues = { "$set": { "nombre": nuevoNombre } }
  mycol.update_one(myquery, newvalues)

def updateDificultadEjercicio(nombre,dificultad):
  myquery = { "nombre": nombre }
  newvalues = { "$set": { "dificultad": dificultad} }
  mycol.update_one(myquery, newvalues)

#Delete
def deleteOneEjercicio(nombre):
  myquery = { "nombre": nombre }
  mycol.delete_one(myquery)

#Mostrar consultas
def MostrarConsultas(mydoc):
  for x in mydoc:
    print(x)
  print()
#Primera insercion de datos

#insertarEjercicio("Sentadilla",1)
#insertarEjercicio("Dominada",2)
#insertarEjercicio("Flexion",3)
#insertarEjercicio("Extension de biceps",2)
#insertarEjercicio("Plancha",4)
#insertarEjercicio("Press de banca",1)
#insertarEjercicio("Remo de espalda baja",1)

#Inserción Adicional
#insertarEjercicio("Extension de gemelos",3)
#insertarEjercicio("Bicicleta",0)

#Tambien se puede hacer así
#mylist = [
#  { "nombre": "Extension de gemelos", "dificultad":3},
#  { "nombre": "Bicicleta", "dificultad":0}]
#x = mycol.insert_many(mylist)

#Updates
"""updateNombreEjercicio("Bicicleta","Bicicleta Estatica")
updateNombreEjercicio("Plancha","Extensión de Tríceps")
updateDificultadEjercicio("Bicicleta Estatica",3)
updateDificultadEjercicio("Plancha",3)
updateNombreEjercicio("Remo de espalda baja","Remo de espalda alta")
updateDificultadEjercicio("Sentadilla",1)
updateDificultadEjercicio("Flexion",2)
"""

#Deletes
""" deleteOneEjercicio("Plancha")
deleteOneEjercicio("Sentadilla")
deleteOneEjercicio("Flexion")
 """

#Consultas avanzadas
MostrarConsultas(mycol.find({ "dificultad": { "$gt": 2 } })) #Muestra las dificultades mayores a 2
MostrarConsultas(mycol.find({ "dificultad": { "$lt": 2 } })) #Muestra las dificultades menores a 2
MostrarConsultas(mycol.find({ "dificultad": 2})) #Muestra las dificultades iguales a 2
MostrarConsultas(mycol.find({ "dificultad" : 1 "&&" : 4})) #Muestra las dificultades mayores que 1 y menores que 4





myclient.close()
