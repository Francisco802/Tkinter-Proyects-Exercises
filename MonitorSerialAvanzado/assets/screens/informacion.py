import tkinter as tk
from tkinter import ttk

class informacion(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Informacion",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Label(
            self,
            text="Version: 2.0 \nHecho por: Jose Francisco Avila",
            font=("Roboto",11)
        ).pack(
            pady=(20,50)
        )

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda: self.manager.pageTohome(),
            width=15
        ).pack(
            pady=10
        )

        #Pruebas

        
        

