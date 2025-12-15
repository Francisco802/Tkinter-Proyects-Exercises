import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from elementos.elementos import elementos



class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        ruta = os.path.dirname(__file__)
        self.title("Radio Buttons")
        self.center_window(self,450,300)
        self.resizable(False,False)

        img=Image.open(os.path.join(ruta,"imagenes\\makima1.png")).resize((16,16))
        icono=ImageTk.PhotoImage(img)

        #icono = tk.PhotoImage(file=r"00AImagenes\makima1.png")
        self.iconphoto(True, icono)
            
        frame = elementos(self)
        frame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )    

    def center_window(self,window,alto,ancho):
        x = (window.winfo_screenwidth() // 2) - (ancho // 2)
        y = (window.winfo_screenheight() // 2) - (alto // 2)

        window.geometry(f'{ancho}x{alto}+{x}+{y}')

