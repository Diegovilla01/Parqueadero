import csv
import os
from datetime import datetime
from utils import log_evento

RUTA_USUARIOS = "src/usuarios.csv"
RUTA_PARQUEO = "src/parqueo.csv"
RUTA_ADMIN = {
    "admin": "1234"
}

def menu_administrador():
    print("\n--- Ingreso Administrador ---")
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if RUTA_ADMIN.get(usuario) != contraseña:
        print("Acceso denegado.")
        log_evento("Intento fallido de acceso a administrador", True)
        return

    log_evento("Acceso administrador exitoso")

    while True:
        print("\n--- Menú de Administración ---")
        print("1. Total vehículos registrados")
        print("2. Total vehículos en parqueo")
        print("3. Total vehículos retirados")
        print("4. Tiempo promedio de parqueo")
        print("5. Lista de usuarios")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total_registrados()
        elif opcion == "2":
            total_en_parqueo()
        elif opcion == "3":
            print("Función aún no implementada.")
        elif opcion == "4":
            tiempo_promedio()
        elif opcion == "5":
            listar_usuarios()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def total_registrados():
    if not os.path.exists(RUTA_USUARIOS):
        print("No hay usuarios registrados.")
        return
    with open(RUTA_USUARIOS) as f:
        total = sum(1 for _ in f)
    print(f"Total usuarios registrados: {total}")
    log_evento("Consulta: total usuarios registrados")

def total_en_parqueo():
    if not os.path.exists(RUTA_PARQUEO):
        print("No hay vehículos actualmente en el parqueadero.")
        return
    with open(RUTA_PARQUEO) as f:
        total = sum(1 for _ in f)
    print(f"Vehículos actualmente en el parqueadero: {total}")
    log_evento("Consulta: total vehículos en parqueo")

def tiempo_promedio():
    if not os.path.exists(RUTA_PARQUEO):
        print("No hay vehículos en parqueo actualmente.")
        return

    total_tiempo = 0
    total_vehiculos = 0
    ahora = datetime.now()

    with open(RUTA_PARQUEO, newline="") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            ingreso = datetime.fromisoformat(fila[1])
            duracion = (ahora - ingreso).total_seconds() / 60  # en minutos
            total_tiempo += duracion
            total_vehiculos += 1

    if total_vehiculos == 0:
        print("No hay vehículos activos.")
        return

    promedio = total_tiempo / total_vehiculos
    print(f"Tiempo promedio de parqueo: {promedio:.2f} minutos")
    log_evento("Consulta: tiempo promedio parqueo")

def listar_usuarios():
    if not os.path.exists(RUTA_USUARIOS):
        print("No hay usuarios registrados.")
        return

    print("\n--- Lista de Usuarios Registrados ---")
    with open(RUTA_USUARIOS, newline="") as archivo:
        reader = csv.reader(archivo)
        for i, fila in enumerate(reader, start=1):
            print(f"{i}. {fila[0]} {fila[1]} - Doc: {fila[2]} - Placa: {fila[3]}")
    log_evento("Consulta: lista usuarios")
