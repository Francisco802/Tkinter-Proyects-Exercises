import tkinter as tk
from tkinter import ttk

class homeScreen(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Menu principal",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Button(
            self,
            text="Conexion",
            style="Accent.TButton",
            command=lambda: self.manager.homeTopage(1), #homeToconexion
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Controles",
            style="Accent.TButton",
            command=lambda: self.manager.homeTopage(2), #homeTocontrol
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Vizualizar",
            style="Accent.TButton",
            command=lambda: self.manager.homeTopage(3), #homeTovizualizar
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Informacion",
            style="Accent.TButton",
            command=lambda: self.manager.homeTopage(4), #homeTovizualizar
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Salir",
            style="Accent.TButton",
            command=self.manager.destroy,
            width=15
        ).pack(
            pady=10
        )
        

