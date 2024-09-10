import json

archivo_canciones = "lista_canciones.json"

def cargar_canciones():
    try:
        with open(archivo_canciones, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def guardar_lista(lista_canciones):
    with open(archivo_canciones, "w") as file:
        json.dump(lista_canciones, file, indent=4)
    
def add_cancion():
    
    lista_canciones = cargar_canciones()
    print()
    print("Para introducir una cancion sigue el formato cancion - autor y la url de youtube")
    print()
    nombre = input("Introduzca titulo - autor de la cancion: ")
    url = input("Introduzca url de la cancion: ")
    cancion = {"numero":" ","nombre":" ","youtube":" "}
    cancion["nombre"] = nombre
    cancion["youtube"] = url
    cancion["numero"] = str(len(lista_canciones)+1)
    
    print(str(len(lista_canciones)+1))
    
    print("La cancion que has incluido.")
    lista_canciones.append(cancion)
    guardar_lista(lista_canciones)
    
    print(cancion["nombre"]," ", cancion["youtube"] )
    print(len(lista_canciones))
    print(lista_canciones[35])
    
    