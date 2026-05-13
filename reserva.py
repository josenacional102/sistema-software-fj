
from excepciones import ReservaError
from logger import registrar_log

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar(self):
        try:
            if self.duracion <= 0:
                raise ReservaError("Duración inválida")

            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as e:
            registrar_log(f"Error en reserva: {str(e)}")
            raise

        else:
            self.estado = "Confirmada"
            return costo

        finally:
            registrar_log("Intento de procesamiento")

    def cancelar(self):
        self.estado = "Cancelada"
