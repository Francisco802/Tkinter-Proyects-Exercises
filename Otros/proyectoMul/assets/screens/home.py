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
            text="Titulo",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Button(
            self,
            text="Boton de prueba 1",
            style="Accent.TButton"

        ).pack()

        ttk.Button(
            self,
            text="Boton de prueba 2"
        ).pack(
            pady=20
        )

        ttk.Checkbutton(
            self,
            text="Button",
            style="Switch"
        ).pack()
        

