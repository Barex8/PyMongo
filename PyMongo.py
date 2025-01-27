import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Creación de la base de datos
mydb = myclient["mydatabase"]