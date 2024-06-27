# Proyecto de Prueba: Conexión de Python con MongoDB

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FMgobeaalcoba%2Fpython_mongoDB&label=Visitors&countColor=%23263759)

Este proyecto es una demostración de cómo conectar una aplicación Python a una base de datos MongoDB utilizando MongoDB Atlas y el paquete `pymongo`.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

1. [Python](https://www.python.org/downloads/) (versión 3.6 o superior)
2. [pip](https://pip.pypa.io/en/stable/installation/)
3. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (Cuenta y Cluster configurados)
4. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (opcional)

## Configuración del Entorno

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local (opcional si decides usar Git):

```bash
git clone https://github.com/Mgobeaalcoba/python_mongoDB
cd tu-repositorio
```

### 2. Crear y Activar un Entorno Virtual

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instalar Dependencias

Instala las dependencias necesarias utilizando pip:

```bash
pip install pymongo python-dotenv
```

### 4. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto y añade las siguientes líneas, reemplazando con tus credenciales:

```env
MONGO_USERNAME=tu_usuario
MONGO_PASSWORD=tu_contraseña
```

### 5. Actualizar el Nombre de la Base de Datos

Asegúrate de reemplazar `"nombre_de_tu_base_de_datos"` en el archivo `main.py` con el nombre real de tu base de datos en MongoDB Atlas.

## Ejecución del Proyecto

Para ejecutar el proyecto, simplemente corre el script `main.py`:

```bash
python main.py
```

Si todo está configurado correctamente, deberías ver el mensaje "Usuario guardado con éxito" en la consola, indicando que el usuario ha sido registrado en la base de datos MongoDB.

## Estructura del Proyecto

```
├── .env                  # Archivo de variables de entorno (no se debe compartir)
├── .gitignore            # Archivos y carpetas que Git debe ignorar
├── README.md             # Documentación del proyecto
├── main.py               # Script principal del proyecto
├── venv/                 # Entorno virtual (no se debe compartir)
```

## Código Principal

A continuación se muestra el código contenido en `main.py`:

```python
import pymongo
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def conectar_db():
    # Obtener el nombre de usuario y la contraseña desde las variables de entorno
    username = os.getenv("MONGO_USERNAME")
    password = os.getenv("MONGO_PASSWORD")
    
    # Crear la cadena de conexión
    uri = f"mongodb+srv://{username}:{password}@cluster0.mongodb.net/test?retryWrites=true&w=majority"
    
    # Conectar al cliente de MongoDB
    cliente = pymongo.MongoClient(uri)
    
    # Conectar a la base de datos (reemplaza "nombre_de_tu_base_de_datos" con el nombre real de tu base de datos)
    db = cliente["nombre_de_tu_base_de_datos"]
    
    return db

class Usuario:
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "edad": self.edad
        }

def guardar_usuario(db, usuario):
    # Conectar a la colección "usuarios" en la base de datos
    coleccion = db["usuarios"]
    
    # Insertar el documento del usuario en la colección
    coleccion.insert_one(usuario.to_dict())
    print("Usuario guardado con éxito")

if __name__ == "__main__":
    # Conectar a la base de datos
    db = conectar_db()
    
    # Crear un nuevo usuario
    nuevo_usuario = Usuario("Juan Pérez", "juan.perez@example.com", 30)
    
    # Guardar el usuario en la base de datos
    guardar_usuario(db, nuevo_usuario)
```

## Notas

- **Seguridad:** No compartas tu archivo `.env` ni tus credenciales en repositorios públicos.
- **Contribuciones:** Si deseas contribuir a este proyecto, siéntete libre de enviar pull requests o reportar issues.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes ver más detalles en el archivo `LICENSE`.
