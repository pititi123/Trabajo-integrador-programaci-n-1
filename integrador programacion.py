"""
Trabajo Práctico Integrador
Materia: Programación
Integrantes: Ignacio Evans

Gestión de Datos de Países en Python
"""

import csv

ARCHIVO_CSV = "paises.csv"


def cargar_csv(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception:
        print("Error al leer el archivo CSV.")

    return paises


def guardar_csv(nombre_archivo, paises):

    campos = ["nombre", "poblacion", "superficie", "continente"]

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


def mostrar_pais(pais):
    print("-" * 50)
    print("Nombre:", pais["nombre"])
    print("Población:", pais["poblacion"])
    print("Superficie:", pais["superficie"], "km²")
    print("Continente:", pais["continente"])


def mostrar_todos(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    for pais in paises:
        mostrar_pais(pais)


def agregar_pais(paises):

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Debe ingresar números válidos.")
        return

    continente = input("Continente: ").strip()

    if continente == "":
        print("El continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_csv(ARCHIVO_CSV, paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):

    nombre = input("Ingrese el país a actualizar: ").strip()

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
            except ValueError:
                print("Valores inválidos.")
                return

            guardar_csv(ARCHIVO_CSV, paises)
            print("País actualizado.")
            return

    print("País no encontrado.")


def buscar_pais(paises):

    texto = input("Ingrese nombre o parte del nombre: ").lower()

    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron resultados.")
        return

    for pais in encontrados:
        mostrar_pais(pais)


def filtrar_continente(paises):

    continente = input("Continente: ").lower()

    encontrados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("Sin resultados.")
        return

    for pais in encontrados:
        mostrar_pais(pais)


def filtrar_poblacion(paises):

    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
    except ValueError:
        print("Valores inválidos.")
        return

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            mostrar_pais(pais)


def filtrar_superficie(paises):

    try:
        minimo = int(input("Superficie mínima: "))
        maximo = int(input("Superficie máxima: "))
    except ValueError:
        print("Valores inválidos.")
        return

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            mostrar_pais(pais)


def ordenar_nombre(paises):

    copia = paises.copy()

    for i in range(len(copia) - 1):
        for j in range(len(copia) - 1 - i):

            if copia[j]["nombre"].lower() > copia[j + 1]["nombre"].lower():
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux

    for pais in copia:
        mostrar_pais(pais)


def ordenar_poblacion(paises):

    opcion = input("Ascendente (A) o Descendente (D): ").upper()

    copia = paises.copy()

    for i in range(len(copia) - 1):
        for j in range(len(copia) - 1 - i):

            condicion = False

            if opcion == "A":
                condicion = copia[j]["poblacion"] > copia[j + 1]["poblacion"]
            elif opcion == "D":
                condicion = copia[j]["poblacion"] < copia[j + 1]["poblacion"]

            if condicion:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux

    for pais in copia:
        mostrar_pais(pais)


def ordenar_superficie(paises):

    opcion = input("Ascendente (A) o Descendente (D): ").upper()

    copia = paises.copy()

    for i in range(len(copia) - 1):
        for j in range(len(copia) - 1 - i):

            condicion = False

            if opcion == "A":
                condicion = copia[j]["superficie"] > copia[j + 1]["superficie"]
            elif opcion == "D":
                condicion = copia[j]["superficie"] < copia[j + 1]["superficie"]

            if condicion:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux

    for pais in copia:
        mostrar_pais(pais)


def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos.")
        return

    mayor = paises[0]
    menor = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n=== ESTADÍSTICAS ===")
    print("Mayor población:", mayor["nombre"], "-", mayor["poblacion"])
    print("Menor población:", menor["nombre"], "-", menor["poblacion"])
    print("Promedio población:", round(suma_poblacion / len(paises), 2))
    print("Promedio superficie:", round(suma_superficie / len(paises), 2))

    print("\nCantidad por continente:")

    for continente in continentes:
        print(continente, ":", continentes[continente])


def menu():

    paises = cargar_csv(ARCHIVO_CSV)

    while True:

        print("\n===== GESTIÓN DE PAÍSES =====")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar por nombre")
        print("8. Ordenar por población")
        print("9. Ordenar por superficie")
        print("10. Mostrar estadísticas")
        print("11. Mostrar todos los países")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_continente(paises)
        elif opcion == "5":
            filtrar_poblacion(paises)
        elif opcion == "6":
            filtrar_superficie(paises)
        elif opcion == "7":
            ordenar_nombre(paises)
        elif opcion == "8":
            ordenar_poblacion(paises)
        elif opcion == "9":
            ordenar_superficie(paises)
        elif opcion == "10":
            mostrar_estadisticas(paises)
        elif opcion == "11":
            mostrar_todos(paises)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


menu()
