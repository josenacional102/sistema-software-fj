
from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class Sala(Servicio):
    def calcular_costo(self, duracion):
        return duracion * 50

    def descripcion(self):
        return "Reserva de sala"


class Equipo(Servicio):
    def calcular_costo(self, duracion):
        return duracion * 30

    def descripcion(self):
        return "Alquiler de equipo"


class Asesoria(Servicio):
    def calcular_costo(self, duracion):
        return duracion * 100

    def descripcion(self):
        return "Asesoría especializada"
