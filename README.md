# PulsePark UdeA – Sistema de Parqueadero

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ![LOGO PEQUENO](https://github.com/user-attachments/assets/1eab9711-bbba-499d-86b4-c3633da5e5bb)


Este proyecto fue desarrollado por estudiantes de Ingeniería Industrial de la Universidad de Antioquia. La idea principal fue crear una aplicación que permita gestionar de forma digital el ingreso y salida de vehículos en el parqueadero de la universidad, reemplazando el proceso manual en papel por uno automatizado y más eficiente.

---

## ¿Quiénes somos?

Somos un grupo de tres estudiantes con distintos roles dentro del desarrollo del sistema:

- **Jeronimo Acevedo Bustamante**: se encargó principalmente del análisis de requisitos y del diseño general del sistema.
- **Diego Antonio Villa Florez**: trabajó en toda la parte de la programación, la lógica del sistema y el backend.
- **Maria Isabel Urrego Jiménez**: se enfocó en las pruebas, documentación y todo lo relacionado con versiones y cambios en el código.

---

## Nuestro enfoque académico

Todos somos del programa de Ingeniería Industrial. Cada uno aportó desde sus fortalezas:

- Jeronimo tiene habilidades para coordinar equipos, analizar requerimientos y planificar.
- Diego domina Python y sabe cómo organizar la lógica de un sistema desde cero.
- Maria es muy detallista con las pruebas, escribe documentación clara y sabe trabajar con Git.

---

## ¿Qué es PulsePark UdeA?

PulsePark UdeA es un programa hecho en Python que corre desde la consola. Permite registrar vehículos, controlar su entrada y salida, calcular cuánto deben pagar, generar facturas y sacar reportes para la administración. Todo queda registrado y se puede exportar en archivos como CSV para análisis.

La idea es que cualquier persona encargada del parqueadero pueda usarlo sin necesidad de tener conocimientos técnicos.

---

## Licencia

El proyecto está bajo la licencia **CC BY-NC-SA 4.0**, lo que significa que cualquiera puede usar y modificar el código, siempre y cuando no sea con fines comerciales y se mantenga la misma licencia.

---

## ¿Por qué lo hicimos?

Nos propusimos mejorar el sistema actual del parqueadero de la universidad, que todavía se hace con papel. Con este programa se puede:

- Registrar a los usuarios y sus vehículos de manera segura.
- Controlar entradas y salidas con tiempos precisos.
- Calcular los pagos según el tiempo que el vehículo estuvo en el parqueadero.
- Sacar reportes de cuánto se ha recaudado o qué tan ocupado está el lugar.
- Generar todo tipo de comprobantes y guardarlos automáticamente.
- Reducir el uso de papel y errores humanos.

Todo esto se hace de forma casi instantánea y con un registro detallado de cada operación.

---

## Funcionalidades principales

- Registro y validación de datos (nombre, documento, placa).
- Ingreso y retiro de vehículos.
- Cálculo automático de tarifas por hora (mínimo una hora).
- Facturas digitales con hora exacta.
- Reportes en tiempo real sobre ocupación y recaudación.
- Exportación de datos a CSV.
- Registro de cada acción con fecha y hora hasta el milisegundo.

---

## Lo que necesitábamos que el programa cumpliera

**Requisitos funcionales:**
- Registro de usuarios.
- Manejo del ingreso y salida de vehículos.
- Cálculo automático de tarifas.
- Reportes administrativos.
- Acceso para administrador con clave.
- Logs de todas las acciones.

**Requisitos no funcionales:**
- Fácil de usar desde la consola.
- Compatible con cualquier sistema operativo.
- Rápido (menos de 0.5 segundos por operación).
- Seguro y confiable, sin pérdida de información.
- Guardado constante de datos.

---

## ¿Cómo organizamos el trabajo?

### Cronograma por semanas:

| Semana | Tarea |
|--------|-------|
| 1 | Revisión de requisitos y diseño inicial |
| 2-3 | Organización del código y estructura |
| 4-5 | Programación de funciones básicas |
| 6 | Pruebas, ajustes y validaciones |
| 7 | Reportes, logs y exportación de datos |
| 8 | Documentación final y entrega |

### Horas invertidas:

- Total de personas: 3  
- Horas por persona: 50  
- Total del proyecto: 150 horas

---
<img width="1300" height="399" alt="chart" src="https://github.com/user-attachments/assets/88adebf6-3f22-49fd-86eb-cee705c45e5f" />



### Primera versión(1.0.0):
El objetivo principal era crear una aplicación sencilla que permitiera gestionar las entradas y salidas de vehículos dentro de un parqueadero. Se utilizó un menú en la consola, fácil de entender, que guiaba al usuario a través de las opciones disponibles. Todo el funcionamiento se basó en condicionales simples (if, elif, else), lo cual facilitaba la lectura y comprensión del código, especialmente para alguien sin mucha experiencia en programación. Pero esta simplicidad también trajo limitaciones, el código era repetitivo, poco flexible, y no estaba preparado para manejar errores o datos de forma eficiente. A pesar de eso, cumplía con lo básico y sirvió como una buena base para comenzar.

### Segunda versión(1.1.0):
En esta versión se realizaron mejoras importantes en la organización del proyecto. Se comenzó a dividir el código en archivos separados, cada uno encargado de una parte específica del sistema, lo cual permitió tener un programa más claro y ordenado. También se añadieron validaciones para evitar errores comunes, como dejar campos vacíos o ingresar valores incorrectos. Además, se empezó a guardar la información en archivos externos, permitiendo conservar los registros entre ejecuciones. Esto mejoró bastante la experiencia del usuario y facilitó la ampliación del proyecto. Aunque seguía siendo una aplicación de consola, se sentía más estable y profesional que la versión anterior.

### Tercera versión(2.0.0):
Esta fue una versión con cambios significativos tanto en la lógica interna como en la presentación general del programa. Se reorganizó por completo el código para hacerlo más compacto, reutilizable y fácil de mantener. Se usaron herramientas más avanzadas y se implementaron buenas prácticas de programación que permitieron reducir errores y mejorar la eficiencia. También se añadió un sistema de registro (logs), lo que permitió guardar información sobre los eventos que ocurren durante el uso del sistema, como entradas y salidas. El menú fue refinado para ofrecer una navegación más fluida, con mensajes claros y respuestas rápidas. Esta versión marcó un paso importante hacia una aplicación mucho más robusta y profesional.

> Este proyecto fue realizado como parte del curso "Algoritmia y Programación 2025-1". Agradecemos a los docentes por su acompañamiento y por permitirnos aplicar lo aprendido en un caso real.
