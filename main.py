
from cliente import Cliente
from servicio import Sala, Equipo, Asesoria
from reserva import Reserva
from excepciones import *
from logger import registrar_log

def ejecutar():
    try:
        c1 = Cliente("Juan", "juan@email.com")
        c2 = Cliente("", "error@email.com")  # Error
    except DatosInvalidosError as e:
        registrar_log(str(e))

    s1 = Sala("Sala VIP")
    s2 = Equipo("Proyector")
    s3 = Asesoria("Consultoría")

    reservas = [
        Reserva(c1, s1, 2),
        Reserva(c1, s2, -1),  # Error
        Reserva(c1, s3, 3)
    ]

    for r in reservas:
        try:
            costo = r.procesar()
            print(f"Reserva confirmada - Costo: {costo}")
        except Exception:
            print("Error procesando reserva")

        finally:
            print("Proceso terminado")

if __name__ == "__main__":
    ejecutar()
