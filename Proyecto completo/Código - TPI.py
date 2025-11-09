#IMPORTACIÓN DEL MÓDULO CSV Y UNICODEDATA PARA NORMALIZACIÓN DE TEXTOS

import csv
import unicodedata

#FUNCIONES DE CARGA Y GUARDADO DE DATOS

def cargar_paises(nombre_archivo): #Cargamos el archivo .CSV y lo convertimos en lista de diccionarios
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "Nombre": fila["Nombre"],
                    "Población": int(fila["Población"]),
                    "Superficie": int(fila["Superficie"]),
                    "Continente": fila["Continente"]
                }
                paises.append(pais)
    except FileNotFoundError: #Advertimos ante la ausencia del archivo
        print(f"❌ No se encontró el archivo '{nombre_archivo}'.")
    return paises


def guardar_paises(nombre_archivo, paises): #Guardamos la lista de países en el .CSV
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["Nombre", "Población", "Superficie", "Continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)


#FUNCIONES AUXILIARES

def normalizar(texto): #Normalizamos el texto para que las búsquedas no sean afectadas por case sensitive
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )

def mostrar_paises(paises): #Definimos la función para mostrar países
    if not paises: #Advertimos ante la búsqueda de un país inexistente
        print("❌ No se encontraron resultados.")
        return

    print(f"\n{'Nombre':25} | {'Población':>12} | {'Superficie':>12} | Continente") #Configuramos el modo de muestra de los países
    print("-" * 70)
    for p in paises:
        poblacion = f"{p['Población']:,}".replace(",", ".") #Reemplazamos la coma por punto para la separación de miles para adaptar la expresión al uso local
        superficie = f"{p['Superficie']:,}".replace(",", ".")
        print(f"{p['Nombre']:25} | {poblacion:>12} | {superficie:>12} | {p['Continente']}")

#FUNCIONES DE BÚSQUEDA Y FILTRADO

def buscar_pais(paises, nombre): #Definimos la función para buscar países
    resultado = []
    nombre_norm = normalizar(nombre)
    for p in paises:
        if nombre_norm in normalizar(p["Nombre"]):
            resultado.append(p)
    return resultado

def filtrar_por_continente(paises, continente): #Definimos la función para filtrar por continente
    resultado = []
    cont_norm = normalizar(continente)
    for p in paises:
        if cont_norm == normalizar(p["Continente"]):
            resultado.append(p)
    return resultado

def filtrar_por_rango(paises, campo, minimo, maximo): #Definimos la función para filtrar por rango
    resultado = []
    for p in paises:
        if minimo <= p[campo] <= maximo:
            resultado.append(p)
    return resultado


#FUNCIÓN PARA ORDENAMIENTO
def ordenar_paises(paises, campo, descendente=False): #Definimos la función para generar el ordenamiento ascendente o descendente
    campo_norm = normalizar(campo)
    def obtener_clave(pais):
        return pais[campo]
    return sorted(paises, key=obtener_clave, reverse=descendente)


# =====================================================
# FUNCIONES DE ESTADÍSTICAS
# =====================================================
def pais_mayor_poblacion(paises): #Definimos la función para mostrar el país con mayor población
    mayor = paises[0]
    for p in paises:
        if p["Población"] > mayor["Población"]:
            mayor = p
    return mayor

def pais_menor_poblacion(paises): #Definimos la función para mostrar el país con menor población
    menor = paises[0]
    for p in paises:
        if p["Población"] < menor["Población"]:
            menor = p
    return menor

def promedio_poblacion(paises): #Definimos la función para mostrar el promedio de población entre todos los países
    total = 0
    for p in paises:
        total += p["Población"]
    return total / len(paises)

def promedio_superficie(paises): #Definimos la función para mostrar el promedio de superficie entre todos los países
    total = 0
    for p in paises:
        total += p["Superficie"]
    return total / len(paises)


def cantidad_por_continente(paises): #Definimos la función para mostrar la cantidad de países de cada continente
    conteo = {}
    for p in paises:
        cont = p["Continente"]
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1
    return conteo


# =====================================================
# FUNCIONES DE MODIFICACIÓN DE DATOS
# =====================================================

def agregar_pais(paises): #Definimos la función para agregar un nuevo país
    nombre = input("Nombre del país: ").strip()
    if buscar_pais(paises, nombre): #Advertimos ante el ingreso de un país ya existente
        print("⚠️ Ese país ya existe en la lista.")
        return

    try: #Solicitud de los datos del nuevo país
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie (km²): "))
        continente = input("Continente: ").strip()
        nuevo = {
            "Nombre": nombre,
            "Población": poblacion,
            "Superficie": superficie,
            "Continente": continente
        }
        paises.append(nuevo) #Agregamos el nuevo país a la lista
        print("✅ País agregado con éxito.")
    except ValueError: #Advertimos ante el ingreso de datos erróneos 
        print("❌ Error: ingrese valores numéricos válidos.")


def actualizar_pais(paises): #Definimos la función para actualizar datos de un país existente
    nombre = input("Ingrese el nombre del país: ").strip()
    encontrados = buscar_pais(paises, nombre)
    if not encontrados: #Advertimos ante el ingreso de un país inexistente en la lista
        print("❌ País no encontrado.")
        return

    pais = encontrados[0]
    print(f"País encontrado: {pais['Nombre']} (Población: {pais['Población']}, Superficie: {pais['Superficie']})")

    try: #Solicitamos los datos a actualizar
        nueva_pob = int(input("Nueva población: "))
        nueva_sup = int(input("Nueva superficie: "))
        pais["Población"] = nueva_pob 
        pais["Superficie"] = nueva_sup
        print("✅ Datos actualizados correctamente.") #Confirmamos la actualización de datos
    except ValueError: #Advertimos ante el ingreso de datos erróneos 
        print("❌ Error: ingrese valores numéricos válidos.")


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

def menu(): #Definimos la función para mostrar el menú
    print("\n" + "="*55)
    print("GESTIÓN DE DATOS DE PAÍSES")
    print("="*55)
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar un nuevo país")
    print("8. Actualizar datos de un país")
    print("9. Salir del programa")
    print("="*55)


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

def main(): #Marcamos la carga del .csv
    archivo = "dataset.csv"
    paises = cargar_paises(archivo)
    if not paises:
        return

    while True: #Definimos que el menú se muestre en forma persistente hasta que el usuario elija salir del programa
        menu() #Llamada a la función del menú
        opcion = input("Seleccione una opción: ").strip() #Solici 

        match opcion: #Generamos un match-case para vincular las funcionalidades con el número de opción elegida
            case "1": #Búsqueda de país por nombre
                print()
                print("1. Buscar país por nombre")
                print()
                nombre = input("Ingrese el nombre del país o una parte de él: ") #Solicitud al usuario para que ingrese el país que desee
                mostrar_paises(buscar_pais(paises, nombre)) #Llamada a la función

            case "2": #Filtrado por continente
                print()
                print("2. Filtrar por continente")
                print()
                cont = input("Ingrese el continente: ") #Solicitud al usuario para que ingrese el continente que desee
                mostrar_paises(filtrar_por_continente(paises, cont)) #Llamada a la función

            case "3": #Filtrado de países por rango de población
                print()
                print("3. Filtrar por rango de población")
                print()
                try:
                    minimo = int(input("Población mínima: ")) #Solicitud al usuario para que ingrese el rango mínimo de población que desea ver
                    maximo = int(input("Población máxima: ")) #Solicitud al usuario para que ingrese el rango máximo de población que desea ver
                    mostrar_paises(filtrar_por_rango(paises, "Población", minimo, maximo)) #Llamada a la función
                except ValueError: #Advertimos ante el ingreso de valores erróneos 
                    print("❌ Ingrese valores numéricos válidos.")

            case "4": #Filtrado de países por rango de superficie
                print()
                print("4. Filtrar por rango de superficie")
                print()
                try:
                    minimo = int(input("Superficie mínima (en kilómetros cuadrados): ")) #Solicitud al usuario para que ingrese el rango mínimo de superficie que desea ver
                    maximo = int(input("Superficie máxima (en kilómetros cuadrados): ")) #Solicitud al usuario para que ingrese el rango máximo de superficie que desea ver
                    mostrar_paises(filtrar_por_rango(paises, "Superficie", minimo, maximo)) #Llamada a la función
                except ValueError: #Advertimos ante el ingreso de valores erróneos 
                    print("❌ Ingrese valores numéricos válidos.")

            case "5": #Ordenamiento de países por campo
                print()
                print("5. Ordenar países")
                print("Seleccione el campo a ordenar (presione N para Nombre, P para Población o S para Superficie):") #Solicitud al usuario simplificada para que elija el campo por el que desea ordenar
                print()

                opcion_campo = input("Opción: ").strip().lower() #Declaramos la variable para que tome la opción elegida
                #Mediante un if-elif-else adaptamos la opción al campo elegido
                if opcion_campo == "n":
                    campo = "Nombre"
                elif opcion_campo == "p":
                    campo = "Población"
                elif opcion_campo == "s":
                    campo = "Superficie"
                else: #Advertimos ante el ingreso de un caracter erróneo
                    print("❌ Opción inválida. Debe ingresar N, P o S.")

                orden = input("Presione A para ascendente o D para descendente: ").strip().lower() #Solicitud al usuario simplificada para que elija orden ascendente o descendente
                print()
                descendente = orden == "d"
                mostrar_paises(ordenar_paises(paises, campo, descendente)) #Llamada a la función
            
            case "6": #Muestra de estadísticas generales
                print()
                print("6. Mostrar estadísticas")
                print()
                mayor = pais_mayor_poblacion(paises) #Llamada a las funciones de mayor y menor población
                menor = pais_menor_poblacion(paises)
                print(f"Mayor población: {mayor['Nombre']} ({mayor['Población']:,})".replace(",", ".")) #Reemplazamos la coma por punto para la separación de miles para adaptar la expresión al uso local
                print(f"Menor población: {menor['Nombre']} ({menor['Población']:,})".replace(",", "."))
                print(f"Promedio población: {promedio_poblacion(paises):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")) #Reemplazamos la coma por punto para la separación de miles y el punto por la coma para decimales para adaptar la expresión al uso local
                print(f"Promedio superficie: {promedio_superficie(paises):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                print("\nCantidad por continente:")
                for cont, cant in cantidad_por_continente(paises).items(): #Llamada a la función de cálculo de países por continente
                    print(f"  {cont}: {cant}")

            case "7": #Ingreso de un nuevo país
                print()
                print("7. Agregar un nuevo país")
                print()
                agregar_pais(paises) #Llamada a la función
                guardar_paises(archivo, paises) #Guardado del nuevo país en la lista

            case "8": #Actualización de datos de un país existente
                print()
                print("8. Actualizar datos de un país")
                print()
                actualizar_pais(paises) #Llamada a la función
                guardar_paises(archivo, paises) #Guardado los datos actualizados en la lista

            case "9": #Salida del programa
                print()
                print("9. Salir del programa")
                print()
                print("👋 ¡Gracias por usar el gestor de países! ¡Hasta la próxima!") #Mensaje de saludo al usuario
                break #Detenemos el despliegue del menú

            case _: #Generamos un case extra ante el caso de que se ingrese un caracter erróneo en las opciones del menú
                print("❌ Opción inválida. Debe ingresar un número entre 1 y 9.")


# =====================================================
# EJECUCIÓN
# =====================================================
if __name__ == "__main__": #Inicio de la ejecución del programa
    main() #Llamada a la función