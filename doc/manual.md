# Manual de Usuario

## Nombre del Sistema
**Sistema de Gestión de Parqueadero PulsePark UdeA**

**Desarrollado por:**  
- Maria Isabel Urrego Jimenez
- Diego Antonio Villa Florez
- Jerónimo Acevedo Bustamante

**Universidad de Antioquia**

**Docente:**  
Julián Andrés Castillo

---

## Objetivo del Sistema

El programa permite gestionar el uso de un parqueadero de automóviles de manera sencilla y controlada, realizando:

- Registro de usuarios.  
- Registro de ingreso y salida de vehículos.  
- Cálculo de cobros según tiempo de parqueo.  
- Emisión de recibos.  
- Generación de reportes administrativos.  
- Exportación de datos a archivos CSV.

---

## Requisitos de Software

- **Lenguaje:** Python 3.8 o superior  
- **Sistema operativo:** Windows, Linux o MacOS  
- **Editor recomendado:** Visual Studio Code  
- **Bibliotecas adicionales:** Solo librerías estándar de Python

---

## Instalación

1. **Descargar el proyecto:**
   ```bash
   [https://github.com/Diegovilla01/Parqueadero]
   ```

2. **Ubicarse en la carpeta del código fuente:**
   ```bash
   cd PulseParkUdeA/src
   ```

3. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

---

## Inicio del Programa

Al iniciar, se mostrará el menú principal con las siguientes opciones:

```
--- PARQUEADERO ---
1. Registrar Usuario  
2. Ingresar Vehículo  
3. Retirar Vehículo  
4. Salir
```

El usuario debe seleccionar la opción deseada escribiendo el número correspondiente y presionando **Enter**.

---

## Funcionalidades Detalladas

### 1. Registrar Usuario

**Descripción:**  
Permite registrar un nuevo usuario del parqueadero.

**Datos solicitados:**
- Nombre: mínimo 3 letras, sin números.  
- Apellido: mínimo 3 letras, sin números.  
- Documento: entre 3 y 15 dígitos numéricos.

**Procedimiento:**
- Seleccionar opción 1.  
- Ingresar cada dato cuando se solicite.  
- Si hay errores, el sistema notificará qué dato es inválido.  
- Al finalizar correctamente, se mostrará un mensaje de confirmación.

---

### 2. Ingresar Vehículo

**Descripción:**  
Registra la entrada de un vehículo al parqueadero.

**Datos solicitados:**
- Documento del usuario registrado.  
- Placa del vehículo (formato ABC123).

**Procedimiento:**
- Seleccionar opción 2.  
- Ingresar el documento del usuario.  
  - Si el usuario no existe, se mostrará un mensaje de error.  
- Ingresar la placa del vehículo.  
  - Debe contener tres letras y tres números.  
- Confirmación de ingreso con hora registrada.

---

### 3. Retirar Vehículo

**Descripción:**  
Registra la salida de un vehículo y calcula el cobro por el tiempo de parqueo.

**Procedimiento:**
- Seleccionar opción 3.  
- Ingresar la placa del vehículo.  
  - Si no está registrada, se mostrará un mensaje de error.  
- El sistema calculará:  
  - Tiempo total transcurrido.  
  - Valor a pagar:  
    - $7.000 por hora completa.  
    - $1.500 por cada cuarto de hora adicional.  
    - Pago mínimo: $7.000.  
- El vehículo se elimina del listado de vehículos en el parqueadero.  
- Se mostrará el recibo con el monto total.

---

### 4. Salir del Sistema

**Descripción:**  
Permite cerrar la aplicación.

**Procedimiento:**
- Seleccionar opción 4.  
- El programa finaliza su ejecución.

---

## Reportes Administrativos

*(Esta sección aplica si se implementa el módulo de administrador)*

Los reportes permiten:

- Consultar cantidad total de vehículos registrados y retirados.  
- Listar vehículos activos en el parqueadero.  
- Ver el total de cobros realizados.  
- Consultar el tiempo promedio de estancia.  
- Identificar el vehículo con mayor y menor tiempo de parqueo.

---

## Exportación de Datos

Los datos podrán exportarse a archivos **CSV** para respaldo y gestión administrativa.

**Archivos generados:**
- Lista de usuarios.  
- Vehículos ingresados y retirados.  
- Historial de cobros.

---

## Registro de Logs

Cada acción realizada quedará registrada en un archivo log con:

- Fecha y hora exactas (con milisegundos).  
- Tipo de acción realizada.  
- Tiempo de ejecución.  
- Datos relevantes (usuario, placa).

---

## Soporte y Contacto

Si presenta inconvenientes, puede contactar al docente o al equipo de desarrollo.

---

## Recomendaciones de Uso

- Mantener el sistema actualizado en su versión más reciente.  
- Verificar que los datos ingresados sean correctos.  
- No apagar el sistema mientras se registran operaciones.  
- Hacer copias de seguridad frecuentes de los archivos CSV y logs.

---

## Licencia

Este proyecto está bajo la licencia **CC BY-NC-SA 4.0**.
