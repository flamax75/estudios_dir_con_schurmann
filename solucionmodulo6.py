import requests


def cargar_datos_liga(url):
    # Obtener los datos JSON de la URL
    response = requests.get(url)
    data = response.json()
    return data


def contar_equipos(data):
    # Contar cuántos equipos han participado en la liga
    return len(data['clubs'])


def mostrar_nombres_y_codigos(data):
    # Mostrar todos los nombres de club y sus códigos de 3 letras
    for club in data['clubs']:
        nombre = club['name']
        # Utilizar get() para manejar el caso donde 'code' no está presente
        codigo = club.get('code', 'N/A')
        print(f"Nombre: {nombre}, Código: {codigo}")


def guardar_datos_en_txt(data, nombre_archivo):
    # Guardar la información en un arcivo TXT
    with open(nombre_archivo, 'w') as file:
        for club in data['clubs']:
            nombre = club['name']
            codigo = club.get('code', 'N/A')
            file.write(f"Nombre: {nombre}, Código: {codigo}\n")


def main():
    # Menú para que el usuario elija la liga
    while True:
        print("\nSeleccione una liga:")
        print("1. Liga alemana")
        print("2. Liga italiana")
        print("3. Liga austríaca")
        print("4. Liga inglesa")
        print("5. Salir")
        opcion = input("Ingrese el número de la liga que desea cargar: ")

        # Mapear la opción del usuario a la URL correspondiente
        ligas = {
            '1': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json',
            '2': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json',
            '3': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json',
            '4': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json',
            '5': 'Salir'
        }

        # Verificar si la opción ingresada es válida
        if opcion not in ligas:
            print("Opción no válida.")
            continue

        # Salir si el usuario elige la opción de salir
        if ligas[opcion] == 'Salir':
            print("Saliendo del programa.")
            break

        # Cargar los datos de la liga seleccionada
        url_liga = ligas[opcion]
        datos_liga = cargar_datos_liga(url_liga)

        # Realizar las tareas solicitadas
        print("\nTareas completadas:")
        print("1. Equipos participantes:", contar_equipos(datos_liga))
        print("2. Nombres de club y códigos:")
        mostrar_nombres_y_codigos(datos_liga)
        print("Datos guardados en arcivo de texto 'equipos_liga.txt'")
        guardar_datos_en_txt(datos_liga, 'equipos_liga.txt')


if __name__ == "__main__":
    main()
