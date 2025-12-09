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
            text="Menu",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Button(
            self,
            text="Entrar",
            style="Accent.TButton",
            command=self.manager.homeTogame

        ).pack()

        ttk.Button(
            self,
            text="Salir",
            command=self.manager.destroy
        ).pack(
            pady=20
        )

        

