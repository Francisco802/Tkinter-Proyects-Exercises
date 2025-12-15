import tkinter as tk
from tkinter import ttk
from assets.screens.pzrraOne import elementos

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana General")
        self.center_window(self,400,800)
        self.resizable(False,False)
        self.icon()
        self.carga_theme()
        self.init_widgets()


    def center_window(self,window,alto,ancho):
        x = (window.winfo_screenwidth() // 2) - (ancho // 2)
        y = (window.winfo_screenheight() // 2) - (alto // 2)

        window.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    def carga_theme(self):
        #thema
        self.forest=ttk.Style(self)
        self.tk.call("source",r"assets\\theme\\Claro\\forest-light.tcl")
        self.forest.theme_use("forest-light")
    
    def icon(self):
        icon=tk.PhotoImage(file="assets\\images\\icon\\makima1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        #contenido
        frame = elementos(self)
        frame.pack(
            side=tk.TOP,
            fill=tk.BOTH
        )
        


         

