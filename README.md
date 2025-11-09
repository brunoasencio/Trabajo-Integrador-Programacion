# ====================================
# Descripción del programa
# ====================================

El proyecto “Gestión de Datos de Países” es una aplicación desarrollada en Python 3 que permite administrar información de países a partir de un archivo CSV.
El sistema fue diseñado para aplicar los principales conceptos aprendidos en la materia Programación, tales como listas, diccionarios, funciones, estructuras condicionales, manejo de archivos y estadísticas básicas.

El programa carga los datos desde un archivo dataset.csv que contiene información sobre el nombre, población, superficie y continente de cada país. Una vez cargados los registros, el usuario puede interactuar mediante un menú en consola para realizar distintas operaciones sobre los datos.
Entre las funcionalidades principales, se incluyen:
 - Búsqueda de países por nombre (coincidencia parcial o exacta).
 - Filtrado por continente, rango de población o rango de superficie.
 - Ordenamiento de los países por nombre, población o superficie (ascendente o descendente).
 - Generación de estadísticas generales del conjunto de datos: país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.
 - Ingreso de nuevos países o actualización de datos de los ya existentes.
 - Manejo de errores robusto para evitar fallos en el ingreso de datos o en la lectura del archivo CSV.

El código se encuentra completamente modularizado, donde cada función cumple una única responsabilidad (lectura de archivos, filtrado, ordenamiento, estadísticas, etc.), lo que facilita su comprensión, mantenimiento y reutilización.
Además, se incorporan validaciones y mensajes claros al usuario, garantizando una experiencia de uso segura y facil.
En resumen, este trabajo refleja una aplicación práctica de los fundamentos de programación estructurada, promoviendo la organización del código, el uso eficiente de las estructuras de datos y la creación de soluciones robustas y legibles.

# ====================================
# Instrucciones de uso
# ====================================

Al ejecutar el programa, se mostrará un menú interactivo en consola con distintas opciones numeradas.
El usuario debe ingresar el número correspondiente a la acción que desea realizar y seguir las indicaciones que aparecen en pantalla.

El menú principal del sistema es el siguiente:
# =======================================================
# GESTIÓN DE DATOS DE PAÍSES
# =======================================================
1. Buscar país por nombre
2. Filtrar por continente
3. Filtrar por rango de población
4. Filtrar por rango de superficie
5. Ordenar países
6. Mostrar estadísticas
7. Agregar un nuevo país
8. Actualizar datos de un país
9. Salir del programa
# =======================================================


A continuación, se detallan las funciones de cada opción:
# 1. Buscar país por nombre
Permite ingresar el nombre de un pais o parte de él, para buscarlo en el listado.
El sistema mostrará todos los países que coincidan parcial o totalmente con el texto ingresado.
Ejemplo: si el usuario escribe arg, se mostrará Argentina.

# 2. Filtrar por continente
Solicita al usuario que ingrese un continente (por ejemplo: América, Europa, Asia, África u Oceanía).
El programa mostrará solo los países pertenecientes al continente indicado.

# 3. Filtrar por rango de población
Permite ingresar una población mínima y una población máxima.
El sistema mostrará todos los países cuya cantidad de habitantes se encuentre dentro de ese rango.
Si se ingresan valores no numéricos, se mostrará un mensaje de error y se pedirá reintentar.

# 4. Filtrar por rango de superficie
Funciona igual que la opción anterior, pero aplicando el filtro sobre la superficie (en km²).
El usuario debe ingresar los valores mínimos y máximos del rango que desea consultar.

# 5. Ordenar países
Permite ordenar el listado completo de países por Nombre, Población o Superficie.
Luego de indicar el campo, el usuario debe elegir si desea un orden ascendente o descendente.
El resultado se muestra en una tabla alineada con columnas para nombre, población, superficie y continente.

# 6. Mostrar estadísticas
Muestra los siguientes indicadores generales:
  - País con mayor población.
  - País con menor población.
  - Promedio de población de todos los países.
  - Promedio de superficie de todos los países.
  - Cantidad de países por continente.

# 7. Salir
Finaliza la ejecución del programa mostrando un mensaje de despedida.

# ====================================
# Ejemplos de entradas y salidas
# ====================================

# 1. Búsqueda por nombre
- Entrada:
Seleccione una opción: 1

1. Buscar país por nombre

Ingrese el nombre del país o una parte de él: argen

Nombre                    |    Población |   Superficie | Continente
----------------------------------------------------------------------
Argentina                 |   47.620.000 |    2.780.400 | América


# 2. Filtrado por continente
- Entrada:
Seleccione una opción: 2

2. Filtrar por continente

Ingrese el continente: europa

- Salida:
Nombre                     |   Población |   Superficie | Continente
----------------------------------------------------------------------
Alemania                   |   83.588.000 |     357.580 | Europa
Francia                    |   66.409.000 |     643.801 | Europa
España                     |   49.316.000 |     505.370 | Europa

# 3. Filtrado por rango de población
- Entrada:
Seleccione una opción: 3

3. Filtrar por rango de población

Población mínima: 50000000
Población máxima: 200000000

- Salida:
Nombre                     |   Población |   Superficie | Continente
----------------------------------------------------------------------
Alemania                   |   83.588.000 |     357.580 | Europa
Francia                    |   66.409.000 |     551,695 | Europa
Brasil                     |  213.421.000 |   8.515.767 | América

# 4. Filtrado por rango de superficie
- Entrada:
Seleccione una opción: 4

4. Filtrar por rango de superficie

Superficie mínima (en kilómetros cuadrados): 10000000
Superficie máxima (en kilómetros cuadrados): 18000000

- Salida:
Nombre                    |    Población |   Superficie | Continente
----------------------------------------------------------------------
Rusia                     |  146.022.000 |   17.098.246 | Asia

# 5. Ordenamiento de países
- Entrada:
Seleccione una opción: 5

5. Ordenar países

Seleccione el campo a ordenar (presione N para Nombre, P para Población o S para Superficie):

Opción: p
Presione A para ascendente o D para descendente: a

- Salida:
Nombre                     |   Población |   Superficie | Continente
----------------------------------------------------------------------
Brasil                     |  213.421.000 |   8.515.767 | América
Japón                      |  123.324.000 |     377.975 | Asia
Alemania                   |   83.588.000 |     357.580 | Europa

# 6. Mostrar estadísticas
- Entrada:
Seleccione una opción: 6

- Salida:

6. Mostrar estadísticas

Mayor población: India (1.417.492.000)
Menor población: Vaticano (1.000)
Promedio población: 40.364.394,18
Promedio superficie: 675.754,59

Cantidad por continente:
  Asia: 49
  Europa: 46
  África: 54
  América: 37
  Oceanía: 14

# 7. Agregar un nuevo país
- Entrada:
Seleccione una opción: 7

7. Agregar un nuevo país

Nombre del país: Groenlandia
Población: 56800
Superficie (km²): 2168000
Continente: América

- Salida:
✅ País agregado con éxito.

# 8. Actualizar datos de un país
- Entrada:
Seleccione una opción: 8

8. Actualizar datos de un país

Ingrese el nombre del país: Belice
País encontrado: Belice (Población: 450000, Superficie: 22970)
Nueva población: 455000
Nueva superficie: 22970

- Salida:
✅ Datos actualizados correctamente.

# 9. Salir del programa
- Entrada:
Seleccione una opción: 9

9. Salir del programa

- Salida:
👋 ¡Gracias por usar el gestor de países! ¡Hasta la próxima!

# 10. Manejo de errores (valor inválido)
- Entrada:
Seleccione una opción: 3
Población mínima: abc
- Salida:
❌ Ingrese valores numéricos válidos.

# ====================================
# Participación de los integrantes
# ====================================

# Bruno Asencio
 - Estructura general del programa y modularización de funciones.
 - Desarrollo del menú principal y estructura de interacción con el usuario.
 - Elaboración del README, ejemplos de entrada y salida, y documentación.
 - Manejo de errores y validaciones en la carga de datos desde CSV.
 - Capturas de pantalla y colaboración en el informe teórico.
 - Revisión general del código y pruebas de funcionamiento.
 - Edicion del video

# Francisco Bacalini
 - Implementación de las funcionalidades de búsqueda, filtrado y ordenamiento.
 - Implementación de las funciones estadísticas.
 - Elaboración del README, ejemplos de entrada y salida, y documentación.
 - Informe teórico.
 - Revisión general del código y pruebas de funcionamiento.
 - Edicion de audio para el video

# Conclusión grupal
Ambos integrantes participaron en la planificación, desarrollo y prueba del programa, aplicando los conceptos de programación estructurada, modularidad y manejo de datos en Python.
La colaboración permitió dividir las tareas de forma equilibrada y lograr un código funcional, legible y bien documentado de manera eficiente y rapida.