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

  
def insertarEjercicio(nombre,dificultad):
    mydict = { "nombre": nombre, "dificultad": dificultad }
    mycol.insert_one(mydict)


def updateNombreEjercicio(nombre,nuevoNombre):
    myquery = { "nombre": nombre }
    newvalues = { "$set": { "nombre": nuevoNombre } }
    mycol.update_one(myquery, newvalues)

def updateDificultadEjercicio(nombre,dificultad):
    myquery = { "nombre": nombre }
    newvalues = { "$set": { "dificultad": dificultad} }
    mycol.update_one(myquery, newvalues)



#Primera insercion de datos

#insertarEjercicio("Sentadilla",1)
#insertarEjercicio("Dominada",2)
#insertarEjercicio("Flexion",3)
#insertarEjercicio("Extension de biceps",2)
#insertarEjercicio("Plancha",4)
#insertarEjercicio("Press de banca",1)
#insertarEjercicio("Remo de espalda baja",1)

#Inserción Adicional
insertarEjercicio("Extension de gemelos",3)
insertarEjercicio("Bicicleta",0)

#Tambien se puede hacer así
#mylist = [
#  { "nombre": "Extension de gemelos", "dificultad":3},
#  { "nombre": "Bicicleta", "dificultad":0}]
#x = mycol.insert_many(mylist)

updateNombreEjercicio("Bicicleta","Bicicleta Estatica")
updateNombreEjercicio("Plancha","Extensión de Tríceps")
updateDificultadEjercicio("Bicicleta","Bicicleta Estatica")
updateNombreEjercicio("Bicicleta","Bicicleta Estatica")



myclient.close()
