import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox

def funcion():
        resultado = MessageBox.askretrycancel("Reintentar",
            "No se puede conectar")
        if resultado == True:
                print("sali verdadero")

ventana=tk.Tk()
ventana.geometry("200x200")

bt=ttk.Button(ventana,text="boton prueba",
            command=funcion)
bt.pack()


ventana.mainloop()