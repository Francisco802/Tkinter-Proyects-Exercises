import tkinter as tk
from tkinter import ttk

class home(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Isobot Controller V2",
            font=("Roboto",16)
        ).pack(
            pady=(20,40)
        )

        ttk.Button(
            self,
            text="Deslizadores",
            command=lambda: self.manager.homeTopage(2),
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Vision Artificial",
            command=lambda: self.manager.homeTopage(4),
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Consola",
            command=lambda: self.manager.homeTopage(3), 
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Configuracion",
            command=lambda: self.manager.homeTopage(1),
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

