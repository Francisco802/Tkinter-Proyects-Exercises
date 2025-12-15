import tkinter as tk
from tkinter import ttk

class salir(tk.Frame):
    def __init__(self,parent,ventana):
        super().__init__(parent)
        self.ventana=ventana
        self.pack(padx=10,pady=10)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.init_widgets()
    
    def init_widgets(self):
        ttk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy
        ).grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )