
import datetime

def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.datetime.now()} - {mensaje}\n")
``
