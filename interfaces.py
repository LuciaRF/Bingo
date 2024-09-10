import tkinter as tk
from tkinter import messagebox

# Función que se ejecutará al hacer clic en el botón
def mostrar_mensaje():
    messagebox.showinfo("Saludo", "¡Hola! Bienvenido a Tkinter")

# Crear la ventana principal
root = tk.Tk()
root.title("Mi primera ventana con Tkinter")  # Título de la ventana
root.geometry("300x200")  # Tamaño de la ventana (ancho x alto)

# Crear un botón y colocarlo en la ventana
boton = tk.Button(root, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack(pady=20)  # `pack` agrega el botón a la ventana y `pady` da espacio alrededor

# Ejecutar la ventana
root.mainloop()