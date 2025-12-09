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
            text="OpenCv Programas",
            font=("Roboto",16)
        ).pack(
            pady=(20,30) #(20,30)
        )

        ttk.Button(
            self,
            text="Umbralizacion",
            width=15,
            command=lambda: self.manager.homeTopage(1)
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Captura de video",
            width=15,
            command=lambda: self.manager.homeTopage(2)
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Colores",
            width=15,
            command=lambda: self.manager.homeTopage(1)
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Caras",
            width=15,
            command=lambda: self.manager.homeTopage(1)
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Objetos",
            width=15,
            command=lambda: self.manager.homeTopage(1)
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Salir",
            style="Accent.TButton",
            width=15,
            command=self.manager.destroy
        ).pack(
            pady=(5,30),
            side="bottom"
        )
    



        

