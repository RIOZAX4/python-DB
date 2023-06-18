from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://<Juan Carlos Rios Aguilar>:<t2duLxRdQ5P2i98n>@cluster0.snpcrsi.mongodb.net/?retryWrites=true&w=majority"

def get_db():
    mongodb_client = MongoClient(MONGODB_URL)
    
    return mongodb_client["academia"]

print("""¿Que deseas hacer?\n 
1 = Mostrar
2 = Agregar
3 = Borrar
4 = Editar
exit = Para salir\n""")

while(True):
    opcion = input("Selecciona una opcion: ")
    print("\n")

    match opcion: 
        
        case"1":
            
            def get():
                database = get_db()

                for item in database.inventory.find():
                    print(item)
                print("\n")
            get()
             
        case"2":
            
            def insert(items: list):
                database = get_db()

                for item in items:
                    database.inventory.insert_one(item)
                print("\n")
            insert([
                {
                    "name": input("Ingresa el producto: "),
                    "category": input("Ingresa la categoria: "),
                    "quantity": input("Ingresa la cantidad: "),
                    "price": input("Ingresa el precio: "),
                }
            ])
            
        case"3":
            
            def delet():
                database = get_db()
                result = database.inventory.delete_one({"name": input("Ingresa el producto que deseas eliminar: ")})
                
                if result.deleted_count > 0:
                    print("Registro eliminado\n")
                else:
                    print("Registro no encontrado\n")
            delet()
            
        case"4":
            
            def edit(filter_query: dict, update_query: dict): 
                database = get_db()
                result = database.inventory.update_one(filter_query, {"$set": update_query})
                
                if result.modified_count > 0:
                    print("Registro editado\n")
                else:
                    print("Registro no encontrado\n")
            
            filter_query = {"name": input("Teclea el producto que quieres modificar: ")}
            update_query = {"name": input("Teclea el producto de remplazo: ")}
            
            edit(filter_query, update_query)
            
        case"exit":
            
            break
        
        case _:
            
            print("Esta no es una de las opciones, intenta de nuevo\n")

