import tkinter as tk

from tkinter.constants import *

def start():
    global horas, minutos, segundos

    #Logica Reloj
    segundos -= 1

    if segundos == 00 and minutos > 00:
        minutos -= 1
        segundos = 60

    if minutos == 00 and segundos == 00:
        horas -= 1
        minutos = 59
        segundos = 60

    #formato reloj
    clock.config(text=f'{horas:02}:{minutos:02}:{segundos:02}')

    #Bucle llamar comenzar de nuevo el metodo cada segundo
    root.after(1000,start) #llamar de nuevo cada segundo

root = tk.Tk()
clock = tk.Label(root, height=1, background="#000000", foreground='white', 
        font=("arial",20), anchor=CENTER, text="00:00:00")

clock.place(relx=0.5, rely=0.5, anchor=CENTER)
horas, minutos, segundos = 4, 0, 4 #inizializo variables globales
start()
root.mainloop()
