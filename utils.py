import os
from datetime import datetime
import platform
import getpass

RUTA_LOG = "logs/eventos.log"

def log_evento(accion, es_error=False):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    ahora = datetime.now()
    timestamp = ahora.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    usuario = getpass.getuser()
    sistema = platform.system()
    version = platform.version()
    separador = " | "

    mensaje = f"{timestamp}{separador}{usuario}{separador}{sistema} {version}{separador}{'ERROR' if es_error else 'INFO'}{separador}{accion}"

    with open(RUTA_LOG, mode="a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")
