
from excepciones import DatosInvalidosError

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()

    def validar(self):
        if not self.__nombre or not self.__email:
            raise DatosInvalidosError("Datos inválidos del cliente")

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"{self.__nombre} - {self.__email}"
