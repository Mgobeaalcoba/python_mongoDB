import pymongo
from model.usuario import Usuario
import os
from dotenv import load_dotenv


def main():
    db = conectar_db()
    
    # Crear un nuevo usuario
    nuevo_usuario = Usuario("Mariano Gonzalez", "mariano.gonzalez@example.com", 40)
    
    # Guardar el usuario en la base de datos
    guardar_usuario(db, nuevo_usuario)


def conectar_db(context="local"):
    if context == "local":
        load_dotenv()
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
        database = os.getenv("MONGO_DATABASE")
    else:
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
        database = os.getenv("MONGO_DATABASE")
        
    cliente = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.gggakxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = cliente[f"{database}"] # Nombre de la base de datos
    return db


def guardar_usuario(db, usuario, context="local"):
    if context == "local":
        load_dotenv()
        coleccion = os.getenv("MONGO_COLLECTION")
    else:
        coleccion = os.getenv("MONGO_COLLECTION")
    
    coleccion = db[f"{coleccion}"] # Nombre de la colección. Si no existe, se crea automáticamente
    coleccion.insert_one(usuario.to_dict())
    print("Usuario guardado con éxito")


if __name__ == "__main__":
    main()