import tkinter as tk
from tkinter import ttk

class logo(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.init_widgets()
    
    def init_widgets(self):
        ttk.Label(
            self,
            text="Animes",
            anchor="center",
            font=("Arial",18)
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )