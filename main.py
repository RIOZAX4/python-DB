from pymongo.mongo_client import MongoClient
import os

MONGODB_URL = "mongodb+srv://academia:polloproxd4@cluster0.snpcrsi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(MONGODB_URL)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def get_db():
    mongodb_client = MongoClient(MONGODB_URL)
    return mongodb_client["Academia"]

def insert(items: list):
    database = get_db()

    for item in items:
        database.inventory.insert_one(item)

def get(filter: dict):
    database = get_db()
    for item in database.inventory.find(filter):
        print(item)

def update(filter: dict, update: dict):
    database = get_db()

    result = database.inventory.update_many(filter, {"$set": update})
    print(f"Se actualizaron {result.modified_count} elementos")

a = 1
while(a):
    print("-----Menú de DB-----\n")
    print("1.- Agregar \n")
    print("2.- Mostrar \n")
    print("3.- Borrar \n")
    print("4.- Editar \n")
    print("5.- Salir \n")
    o = input("Seleccione una opción... ")

    if o == '1':
        print("Haz seleccionado la opción de Agregar datos")
        insert([
            {
                "name" : input("\nNombre del producto: "),
                "category" : input("Categoría del producto: "),
                "quantity" : int(input("Cantidad del producto: ")),
                "price" : int(input("Precio del producto: ")),
            },
        ])
        print("Haz agregado un elemento más ^-^")
        os.system('pause')

    elif o == '2':
        print("Haz seleccionado la opción de Mostrar datos")
        oo = input("Qué deseas encontrar(blancos ó cocina)? ")
        if oo == 'blancos':
            get({"category": "blancos"})
        elif oo == 'cocina':
            get({"category":"cocina"})
        os.system('pause')

    elif o == '3':
        b = 1
        while(b):
            print("Haz seleccionado la opción de Borrar datos\n")
            database = get_db()
            print("Presiona 's' para salir")
            delete = input("Qué producto deseas eliminar? ")
            borrar = database.inventory.delete_one({"name": delete})
            if delete == 's':
                print("adioh")
                b = 0
            else:
                if borrar.deleted_count > 0: #el deleted_count es para saber cuántos objetos se han seleccionado para eliminar
                    print("[" + str(delete) + "] ha sido elimiado correctamente °-° \n")
                else:
                    print("Ese producto no existe :C")
        os.system('pause')

    elif o == '4':
        print("Haz seleccionado la opción de Editar datos (nombre)")
        update(filter={"name": input("Qué deseas editar? ")}, update={"name" : input("\nNombre del producto: "),
                                                                      "category" : input("Categoría del producto: "),
                                                                      "quantity" : int(input("Cantidad del producto: ")),
                                                                      "price" : int(input("Precio del producto: ")),
                                                                      },)
        os.system('pause')

    elif o == '5':
        print("Te has salido de la base de datos")
        os.system('pause')
        a = 0
    os.system('cls')

