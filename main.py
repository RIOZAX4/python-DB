from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://<Juan Carlos Rios Aguilar>:<t2duLxRdQ5P2i98n>@cluster0.snpcrsi.mongodb.net/?retryWrites=true&w=majority"

def get_db():
    mongodb_client = MongoClient(MONGODB_URL)
    return mongodb_client["Academia"]

def insert(items: list):
    database = get_db()

    for item in items:
        database.insert_one(item)

insert([
    {
        "name" : "Tenedor",
        "category" : "cocina",
        "quantity" : 20,
        "price" : 5,
    },
    {
        "name" : "Cuchara",
        "category" : "cocina",
        "quantity" : 10,
        "price" : 3,
    },
    {
        "name" : "Papel de baño",
        "category" : "blancos",
        "quantity" : 50,
        "price" : 15,
    },
])


