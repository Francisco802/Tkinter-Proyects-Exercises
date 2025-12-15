import tkinter as tk
from tkinter import ttk
from components.opciones import opciones

class oneExample(tk.Tk):
    def __init__(self,*args,**kwargs):       #no es necesario *args,**kwargs
        super().__init__(*args,**kwargs)
        self.title("Modificar Texto")
        self.center_window(self,400,300)     #Centrar ventana en pantalla
        self.resizable(False, False)         #No redimencionar la ventana

        frame=opciones(self)
        frame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

    def center_window(self,window,alto,ancho):
        # Obtener las dimensiones de la pantalla
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calcular la posición para centrar la ventana
        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        # Establecer la geometría de la ventana
        window.geometry(f'{ancho}x{alto}+{x}+{y}')