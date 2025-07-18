from usuario import registrar_usuario
from parqueadero import ingresar_vehiculo, retirar_vehiculo
from admin import menu_administrador
from utils import log_evento

def menu():
    while True:
        print("\n--- PARQUEADERO PulsePark UdeA ---")
        print("1. Registrar usuario")
        print("2. Ingresar vehículo")
        print("3. Retirar vehículo")
        print("4. Administrador")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            ingresar_vehiculo()
        elif opcion == "3":
            retirar_vehiculo()
        elif opcion == "4":
            menu_administrador()
        elif opcion == "5":
            log_evento("Cerrar programa")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
