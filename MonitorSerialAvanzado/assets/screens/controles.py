import tkinter as tk
from tkinter import ttk

class controles(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Controles",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Button(
            self,
            text="Switch mode",
            #style="Accent.TButton",
            command=lambda: self.manager.controlTopage(1),
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Controller mode",
            #style="Accent.TButton",
            command=lambda: self.manager.controlTopage(2),
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Terminal mode",
            #style="Accent.TButton",
            command=lambda: self.manager.controlTopage(3),
            width=15
        ).pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda:self.manager.pageTohome(),
            width=15
        ).pack(
            pady=10
        )
        

