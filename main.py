import pymongo
from model.usuario import Usuario
import os
from dotenv import load_dotenv


def main():
    db = conectar_db()
    
    # Crear un nuevo usuario
    nuevo_usuario = Usuario("Juan Pérez", "juan.perez@example.com", 30)
    
    # Guardar el usuario en la base de datos
    guardar_usuario(db, nuevo_usuario)


def conectar_db(context="local"):
    if context == "local":
        load_dotenv()
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
    else:
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
        
    cliente = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.gggakxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = cliente["ProjectTest"] # Nombre de la base de datos
    return db


def guardar_usuario(db, usuario):
    coleccion = db["usuarios"] # Nombre de la colección. Si no existe, se crea automáticamente
    coleccion.insert_one(usuario.to_dict())
    print("Usuario guardado con éxito")


if __name__ == "__main__":
    main()