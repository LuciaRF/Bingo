import random
import webbrowser
import load_funciones

lista_canciones = load_funciones.cargar_canciones()

print("Bienvenidos al Bingo musical: ")

num_jugadores = int (input("Cuantos jugadores vais a participar? "))

#clase jugador
class Jugador:
    def __init__(self,lista_canciones):
        self.lista_canciones = lista_canciones
        
        if len(self.lista_canciones) >= 15:
            
            lista = [x["nombre"] for x in self.lista_canciones]        
            self.tablero = random.sample(lista,15)
    
    def imprimir_tablero(self):
        for i,cancion in enumerate(self.tablero):
        
            if i%5==0:
                print()
                print(cancion," || ", end="\t")
            else:
                print(cancion, "||", end="\t")
                
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
        print("\n",self.lista_canciones[numero]["nombre"],"\n")
        play = Reproductor(self.lista_canciones[numero]["youtube"])
        play.reproducir()
        

lista_jugadores = [Jugador(lista_canciones) for _ in range(num_jugadores)]

for index,jugador in enumerate(lista_jugadores):
    print("\nJugador: "+ str(index +1))
    
    jugador.imprimir_tablero()
    
n = 0

bingo = Bingo(lista_canciones)

while n != 3:
    print("Empezamos!!!")
    print("-------------------")
    print("1. Sacar cancion: ")
    print("2. Incluir cancion")
    print("3. Salir")
    n = int (input("Que quieres hacer? "))
    
    if(n == 1):
        bingo.sacar_cancion()
    elif(n == 2):
        load_funciones.add_cancion()
        


    

       

