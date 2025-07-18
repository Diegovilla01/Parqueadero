import csv
import re
from utils import log_evento

RUTA_USUARIOS = "src/usuarios.csv"

def validar_nombre(nombre):
    nombre = nombre.replace(" ", "")
    return len(nombre) >= 3 and nombre.isalpha()

def validar_apellido(apellido):
    apellido = apellido.replace(" ", "")
    return len(apellido) >= 3 and apellido.isalpha()

def validar_documento(documento):
    return documento.isdigit() and 3 <= len(documento) <= 15

def validar_placa(placa):
    return bool(re.match(r'^[A-Z]{3}[0-9]{3}$', placa.upper()))

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    documento = input("Documento: ").strip()
    placa = input("Placa del vehículo (ej: ABC123): ").strip().upper()

    errores = []

    if not validar_nombre(nombre):
        errores.append("El nombre debe tener mínimo 3 letras y sin números.")
    if not validar_apellido(apellido):
        errores.append("El apellido debe tener mínimo 3 letras y sin números.")
    if not validar_documento(documento):
        errores.append("El documento debe tener entre 3 y 15 dígitos numéricos.")
    if not validar_placa(placa):
        errores.append("La placa debe tener 3 letras seguidas de 3 números (ej: ABC123).")

    if errores:
        print("\nSe encontraron los siguientes errores:")
        for error in errores:
            print(f"- {error}")
        log_evento("Error al registrar usuario", True)
        return

    with open(RUTA_USUARIOS, mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, apellido, documento, placa])
    
    print(" Usuario registrado exitosamente.")
    log_evento(f"Usuario registrado: {nombre} {apellido} - Placa {placa}")
