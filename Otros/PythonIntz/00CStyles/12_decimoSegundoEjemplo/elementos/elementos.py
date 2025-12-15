import tkinter as tk
from tkinter import ttk
import os
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        ruta = os.path.realpath(".")
        self.ventana=ventana

        #Stilo con un paquete de temas
        self.forest = ttk.Style(self.ventana)
        #direct=os.path.join(ruta,"_internal\\forest-light.tcl")
        direct=r"forest-light.tcl"

        self.ventana.tk.call("source",direct)       
        self.forest.theme_use("forest-light")       
        
        self.init_widgets()

    def init_widgets(self):
        ttk.Button(
            self,
            text="Buscar archivo",
            style='Accent.TButton'
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Guardar archivo"
        ).pack(
            **styles.PACK
        )

        ttk.Checkbutton(
            self,
            text="Cambiar fuente",
            style='ToggleButton'
        ).pack(
            **styles.PACK
        )

        ttk.Checkbutton(
            self,
            text="Cambiar color",
            style='Switch'
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show info"
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show warning"
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show error"
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askokquestion"
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askokcancel"
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askretrycancel"
        ).pack(
            **styles.PACK
        )
        



