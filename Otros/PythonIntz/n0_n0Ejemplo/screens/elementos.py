import tkinter as tk
from tkinter import ttk

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Ejemplo de etiqueta",
            padding=20
        ).pack(
            pady=20
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
        



