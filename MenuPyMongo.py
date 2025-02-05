import pymongo
import pymongo.collection
import pymongo.database
#Importar con: "python -m pip install pymongo" en el cmd
mycol = pymongo
mydb = pymongo.database
myclient = pymongo.MongoClient()
def conexion():
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  #Creación de la base de datos
  print(myclient.list_database_names())

  dblist = myclient.list_database_names()
  if "Ejercicio" in dblist:
    print("La base de datos existe")
  print(myclient)
  return myclient

def crearColeccion(nombre_coleccion):
  print(myclient)
  #Creación de la base de datos
  mydb = myclient["Ejercicio"]
  mycol = mydb[nombre_coleccion]

  collist = mydb.list_collection_names()
  if nombre_coleccion in collist:
    print("The collection exists.")
  return mycol

#Insertar  
""" def insertarDocumento(sentencia):
  #"nombre": nombre, "dificultad": dificultad 
  mydict = {sentencia}
  mycol.insert_one(mydict) """

def insertarDocumento(nombre,dificultad):
  mydict = { "nombre": nombre, "dificultad": dificultad }
  mycol.insert_one(mydict)

#Update
def updateNombreEjercicio(nombre,nuevoNombre):
  myquery = { "nombre": nombre }
  newvalues = { "$set": { "nombre": nuevoNombre } }
  mycol.UpdateOne(myquery, newvalues)

def updateDescripcionDocumento(nombre,dificultad):
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
respuesta = 0
while(respuesta != 6):
    print("------------------ PyMongo ------------------")
    print("1. Conexion a la base de datos")
    print("2. Crear una colección en la base de datos")
    print("3. Creación de documentos")
    print("4. Busqueda de documentos")
    print("5. Actualizar documentos")
    print("6. Terminar conexión base de datos")
    respuesta = int(input("Inserte un valor: "))

    if respuesta == 1:
       #No se pueden hacer metodos porque las variables no son mutables
       myclient = pymongo.MongoClient("mongodb://localhost:27017/")
       #Creación de la base de datos
       dblist = myclient.list_database_names()
       if "Ejercicio" in dblist:
         print("La base de datos existe")

    elif respuesta == 2:
        nombreColeccion = input("Inserte el nombre de la nueva colección: ")
        
        mydb = myclient["Ejercicio"]
        mycol = mydb[nombreColeccion]

        collist = mydb.list_collection_names()
        if nombreColeccion in collist:
            print("The collection exists.")
        
    elif respuesta == 3:
        print("Inserte una sentencia para crear documentos, Ejemplo: "+"nombre:Nombre, descripcion: Esto es una descripcion")
        nombre = input("Nombre: ")
        descripcion = input("Descripcion: ")

        insertarDocumento(nombre,descripcion)

    elif respuesta == 4:
       nombreCampo = input("Inserte el nombre del campo: ")
       valor = input("Ingrese el valor que esta buscado del campo: ")
       MostrarConsultas(mycol.find({ nombreCampo : valor}))

    elif respuesta == 5:
       nombreCampo = input("Ingrese el nombre del documento que quiere editar: ")
       valor = input("Ingrese el nueva valor de la descripcion: ")
       updateDescripcionDocumento(nombreCampo,valor)

    elif respuesta == 6:
       myclient.close()
      
  
