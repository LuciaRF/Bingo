import random
import webbrowser
import load_funciones

import tkinter as tk
from tkinter import messagebox

import os
import sys
import json

[
    {
        "numero": "1",
        "nombre": "Opening Digimon 1",
        "youtube": "https://www.youtube.com/watch?v=UXwunDD5Lm8"
    },
    {
        "numero": "2",
        "nombre": "Con Valor - Mulan",
        "youtube": "https://www.youtube.com/watch?v=Eq_4yD4ROlo"
    },
    {
        "numero": "3",
        "nombre": "Opening Digimon 2",
        "youtube": "https://www.youtube.com/watch?v=d5Bc16yQLcI"
    },
    {
        "numero": "4",
        "nombre": "Opening Pokemon",
        "youtube": "https://www.youtube.com/watch?v=XNF_xnmKuRI"
    },
    {
        "numero": "5",
        "nombre": "Poke Rap",
        "youtube": "https://www.youtube.com/watch?v=gWzHLrLGVSA"
    },
    {
        "numero": "6",
        "nombre": "Opening Pepper Ann",
        "youtube": "https://www.youtube.com/watch?v=RY-n7o1SeoA"
    },
    {
        "numero": "7",
        "nombre": "Opening Carmen San Diego",
        "youtube": "https://www.youtube.com/watch?v=XLSp29Zx6Ck"
    },
    {
        "numero": "8",
        "nombre": "Opening Chicho Terremoto",
        "youtube": "https://www.youtube.com/watch?v=0I5l6N_cIL0"
    },
    {
        "numero": "9",
        "nombre": "Opening La familia crece",
        "youtube": "https://www.youtube.com/watch?v=lOYlPmXxnfk"
    },
    {
        "numero": "10",
        "nombre": "Opening Sakura",
        "youtube": "https://www.youtube.com/watch?v=QDezQD57h-g"
    },
    {
        "numero": "11",
        "nombre": "Opening Dragon Ball",
        "youtube": "https://www.youtube.com/watch?v=dtD_xGvkWLk"
    },
    {
        "numero": "12",
        "nombre": "Opening Dragon Ball Z",
        "youtube": "https://www.youtube.com/watch?v=3HT60PKvrfM"
    },
    {
        "numero": "13",
        "nombre": "Opening Dragon Ball GT",
        "youtube": "https://www.youtube.com/watch?v=eEh8yzkFd8I"
    },
    {
        "numero": "14",
        "nombre": "Faint - Linkin Park",
        "youtube": "https://www.youtube.com/watch?v=LYU-8IFcDPw"
    },
    {
        "numero": "15",
        "nombre": "Complicated - Avril Lavigne",
        "youtube": "https://www.youtube.com/watch?v=5NPBIwQyPWE"
    },
    {
        "numero": "16",
        "nombre": "EveryBody - Backstreet Boys",
        "youtube": "https://youtu.be/e-syzbglE6g?si=4rkcunrKNBFAVCWT&t=40"
    },
    {
        "numero": "17",
        "nombre": "Wannabe - Spice Girls",
        "youtube": "https://www.youtube.com/watch?v=HNehiNC_tq0"
    },
    {
        "numero": "18",
        "nombre": "Rolling In The Deep - Adele",
        "youtube": "https://www.youtube.com/watch?v=rYEDA3JcQqw"
    },
    {
        "numero": "19",
        "nombre": "Set Fire to the Rain - Adele",
        "youtube": "https://www.youtube.com/watch?v=a2giXO6eyuI"
    },
    {
        "numero": "20",
        "nombre": "The Reason - Hoobastank",
        "youtube": "https://www.youtube.com/watch?v=fV4DiAyExN0"
    },
    {
        "numero": "21",
        "nombre": "In The End - Linkin Park",
        "youtube": "https://www.youtube.com/watch?v=eVTXPUF4Oz4"
    },
    {
        "numero": "22",
        "nombre": "Holiday - Green Day",
        "youtube": "https://www.youtube.com/watch?v=l2hA8g1cNvQ"
    },
    {
        "numero": "23",
        "nombre": "Welcome To The Black Parade - My Chemical Romance",
        "youtube": "https://www.youtube.com/watch?v=Rwaoq2fyPPw"
    },
    {
        "numero": "24",
        "nombre": "Boy with luv - BTS",
        "youtube": "https://www.youtube.com/watch?v=i4ywHpSXThs"
    },
    {
        "numero": "25",
        "nombre": "We Will Rock You - Queen",
        "youtube": "https://www.youtube.com/watch?v=-tJYN-eG1zk"
    },
    {
        "numero": "26",
        "nombre": "Bohemian Rhapsody - Queen",
        "youtube": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"
    },
    {
        "numero": "27",
        "nombre": "Thriller - Michael Jackson",
        "youtube": "https://www.youtube.com/watch?v=-e-y-1VRZ3I"
    },
    {
        "numero": "28",
        "nombre": "Smells Like Teen Spirit - Nirvana",
        "youtube": "https://www.youtube.com/watch?v=-e-y-1VRZ3I"
    },
    {
        "numero": "29",
        "nombre": "Dancing Queen - ABBA",
        "youtube": "https://www.youtube.com/watch?v=xFrGuyw1V8s"
    },
    {
        "numero": "30",
        "nombre": "Mamma Mia - ABBA",
        "youtube": "https://www.youtube.com/watch?v=unfzfe8f9NI"
    },
    {
        "numero": "31",
        "nombre": "Mi Gran Noche - Raphael",
        "youtube": "https://www.youtube.com/watch?v=477d0T1YuKE"
    },
    {
        "numero": "32",
        "nombre": "Ave Maria - David Bisbal",
        "youtube": "https://www.youtube.com/watch?v=gra-sIV1n4U"
    },
    {
        "numero": "33",
        "nombre": "Barbie Girl - Aqua",
        "youtube": "https://www.youtube.com/watch?v=ZyhrYis509A"
    },
    {
        "numero": "34",
        "nombre": "Cuando tu vas - Chenoa",
        "youtube": "https://www.youtube.com/watch?v=ZyhrYis509A"
    },
    {
        "numero": "35",
        "nombre": "Libre - Nino Bravo",
        "youtube": "https://www.youtube.com/watch?v=TQkAIx4YjSo"
    }
]

def obtener_ruta_archivo(nombre_archivo):
    if hasattr(sys, '_MEIPASS'):
        # Si se está ejecutando desde el ejecutable
        return os.path.join(sys._MEIPASS, nombre_archivo)
    else:
        # Si se está ejecutando desde el script original
        return os.path.join(os.path.dirname(__file__), nombre_archivo)

archivo_canciones = obtener_ruta_archivo("lista_canciones.json")

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
    # print()
    # print("Para introducir una cancion sigue el formato cancion - autor y la url de youtube")
    # print()
    nombre = input("Introduzca titulo - autor de la cancion: ")
    url = input("Introduzca url de la cancion: ")
    cancion = {"numero":" ","nombre":" ","youtube":" "}
    cancion["nombre"] = nombre
    cancion["youtube"] = url
    cancion["numero"] = str(len(lista_canciones)+1)
    
    # print(str(len(lista_canciones)+1))
    
    # print("La cancion que has incluido.")
    lista_canciones.append(cancion)
    guardar_lista(lista_canciones)
    
    # print(cancion["nombre"]," ", cancion["youtube"] )
    # print(len(lista_canciones))
    # print(lista_canciones[35])

lista_canciones = cargar_canciones()

#clase jugador
class Jugador:
    def __init__(self,lista_canciones):
        self.lista_canciones = lista_canciones
        
        if len(self.lista_canciones) >= 15:
            
            lista = [x["nombre"] for x in self.lista_canciones]        
            self.tablero = random.sample(lista,15)
    
    # def imprimir_tablero(self):
    #     for i,cancion in enumerate(self.tablero):
        
    #         if i%5==0:
    #             print()
    #             print(cancion," || ", end="\t")
    #         else:
    #             print(cancion, "||", end="\t")
    def imprimir_tablero(self):
        return "\n".join(self.tablero)
                
class Reproductor:
    def __init__(self,url_cancion):
        self.url_cancion = url_cancion
    
    def reproducir(self):
        webbrowser.open_new(self.url_cancion)
        
                      
class Bingo:
    def __init__(self,lista_canciones):
        self.lista_canciones = lista_canciones
        self.canciones = [x["numero"] for x in self.lista_canciones]
        self.tamano = len(lista_canciones)
        self.numeros = [i for i in range(self.tamano)]
    
    def borrar_cancion(self,numero):
        self.numeros.remove(numero)
        
    def sacar_cancion(self):
        numero = random.choice(self.numeros)
        self.borrar_cancion(numero)
        #print("\n",self.lista_canciones[numero]["nombre"],"\n")
        # play = Reproductor(self.lista_canciones[numero]["youtube"])
        # play.reproducir()
        cancion = self.lista_canciones[numero]
        return cancion
        

# lista_jugadores = [Jugador(lista_canciones) for _ in range(num_jugadores)]

# for index,jugador in enumerate(lista_jugadores):
#     print("\nJugador: "+ str(index +1))
    
#     jugador.imprimir_tablero()
    
# n = 0

# bingo = Bingo(lista_canciones)

# while n != 3:
#     print("Empezamos!!!")
#     print("-------------------")
#     print("1. Sacar cancion: ")
#     print("2. Incluir cancion")
#     print("3. Salir")
#     n = int (input("Que quieres hacer? "))
    
#     if(n == 1):
#         bingo.sacar_cancion()
#     elif(n == 2):
#         load_funciones.add_cancion()
        

# Interfaz gráfica
class BingoGUI:
    def __init__(self, root):
        self.root = root
        self.bingo = Bingo(lista_canciones)
        self.lista_jugadores = []

        # Configuración de la ventana principal
        self.root.title("Bingo Musical")
        self.root.geometry("600x400")

        # Etiqueta de bienvenida
        self.label_bienvenida = tk.Label(root, text="Bienvenidos al Bingo Musical", font=("Helvetica", 16))
        self.label_bienvenida.pack(pady=10)

        # Entrada para número de jugadores
        self.label_num_jugadores = tk.Label(root, text="¿Cuántos jugadores van a participar?")
        self.label_num_jugadores.pack()
        self.entry_num_jugadores = tk.Entry(root)
        self.entry_num_jugadores.pack()

        # Botón para iniciar el juego
        self.boton_iniciar = tk.Button(root, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=10)

        # Área de texto para mostrar los tableros de jugadores
        self.text_tableros = tk.Text(root, height=10, width=50)
        self.text_tableros.pack(pady=10)

        # Botón para sacar una canción
        self.boton_sacar_cancion = tk.Button(root, text="Sacar Canción", command=self.sacar_cancion, state=tk.DISABLED)
        self.boton_sacar_cancion.pack(pady=5)

        # Botón para incluir canción
        self.boton_incluir_cancion = tk.Button(root, text="Incluir Canción", command=self.incluir_cancion)
        self.boton_incluir_cancion.pack(pady=5)

    def iniciar_juego(self):
        try:
            num_jugadores = int(self.entry_num_jugadores.get())
            self.lista_jugadores = [Jugador(lista_canciones) for _ in range(num_jugadores)]
            self.mostrar_tableros()
            self.boton_sacar_cancion.config(state=tk.NORMAL)
        except ValueError:
            self.mostrar_mensaje("Error", "Por favor, ingresa un número válido de jugadores.")

    def mostrar_tableros(self):
        self.text_tableros.delete(1.0, tk.END)
        for index, jugador in enumerate(self.lista_jugadores):
            self.text_tableros.insert(tk.END, f"\nJugador {index + 1}:\n{jugador.imprimir_tablero()}\n")

    def sacar_cancion(self):
        cancion = self.bingo.sacar_cancion()
        self.mostrar_mensaje("Canción Seleccionada", f"Nombre: {cancion['nombre']}\nURL: {cancion['youtube']}")
        Reproductor(cancion['youtube']).reproducir()

    def incluir_cancion(self):
        load_funciones.add_cancion()
        self.bingo = Bingo(load_funciones.cargar_canciones())
        self.mostrar_mensaje("Canción Añadida", "La canción ha sido añadida a la lista.")

    def mostrar_mensaje(self, titulo, mensaje):
        tk.messagebox.showinfo(titulo, mensaje)

# Inicialización de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BingoGUI(root)
    root.mainloop()
    

       

