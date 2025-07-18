import csv
import os
from datetime import datetime
from utils import log_evento

RUTA_USUARIOS = "src/usuarios.csv"
RUTA_PARQUEO = "src/parqueo.csv"

TARIFA_HORA = 7000
TARIFA_CUARTO = 1500

def cargar_usuarios():
    usuarios = {}
    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, newline="") as archivo:
            reader = csv.reader(archivo)
            for nombre, apellido, doc, placa in reader:
                usuarios[placa] = {"nombre": nombre, "apellido": apellido, "documento": doc}
    return usuarios

def ingresar_vehiculo():
    print("\n--- Ingreso de Vehículo ---")
    placa = input("Ingrese la placa del vehículo: ").strip().upper()
    usuarios = cargar_usuarios()

    if placa not in usuarios:
        print("Usuario no registrado. Registre el usuario antes de ingresar el vehículo.")
        log_evento(f"Fallo ingreso vehículo: placa {placa} no registrada", True)
        return

    # Revisar si el vehículo ya está en el parqueadero
    if os.path.exists(RUTA_PARQUEO):
        with open(RUTA_PARQUEO, newline="") as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                if fila[0] == placa:
                    print("Este vehículo ya está dentro del parqueadero.")
                    return

    ahora = datetime.now()
    with open(RUTA_PARQUEO, mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([placa, ahora.isoformat()])
    
    print(" Vehículo ingresado con éxito.")
    log_evento(f"Ingreso vehículo: placa {placa}")

def retirar_vehiculo():
    print("\n--- Retiro de Vehículo ---")
    placa = input("Ingrese la placa del vehículo: ").strip().upper()

    if not os.path.exists(RUTA_PARQUEO):
        print("No hay vehículos registrados actualmente.")
        return

    filas = []
    encontrado = False
    tiempo_ingreso = None

    with open(RUTA_PARQUEO, newline="") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if fila[0] == placa:
                encontrado = True
                tiempo_ingreso = datetime.fromisoformat(fila[1])
            else:
                filas.append(fila)

    if not encontrado:
        print("Vehículo no encontrado en el parqueadero.")
        return

    ahora = datetime.now()
    duracion = ahora - tiempo_ingreso
    minutos = duracion.total_seconds() / 60
    horas_enteras = int(minutos // 60)
    minutos_restantes = minutos % 60
    cuartos_hora = int((minutos_restantes + 14) // 15)

    total = horas_enteras * TARIFA_HORA + cuartos_hora * TARIFA_CUARTO
    if total < TARIFA_HORA:
        total = TARIFA_HORA

    with open(RUTA_PARQUEO, mode="w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(filas)

    print(f"Tiempo total: {int(minutos)} minutos")
    print(f"Total a pagar: ${total}")
    log_evento(f"Retiro vehículo: placa {placa}, duración {int(minutos)} minutos, total ${total}")
