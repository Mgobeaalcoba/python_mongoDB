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
