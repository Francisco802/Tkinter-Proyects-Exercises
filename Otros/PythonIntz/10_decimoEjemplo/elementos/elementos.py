import tkinter as tk
from tkinter import ttk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.init_widgets()

    def init_widgets(self):
        tabControl=ttk.Notebook(self)

        tab1=ttk.Frame(tabControl)
        tab2=ttk.Frame(tabControl)
        tab3=ttk.Frame(tabControl)

        tabControl.add(tab1, text ='Tab 1')
        tabControl.add(tab2, text ='Tab 2') 
        tabControl.add(tab3, text ='Tab 3') 
        tabControl.pack(expand = 1, fill ="both") 

        tk.Label(
            tab1,
            text="Hola a todos"
        ).pack()

        tk.Label(
            tab2,
            text="Fubuki good"
        ).pack()

        tk.Label(
            tab3,
            text="Makima Good"
        ).pack()

        tk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy
        ).pack(
            padx=20,
            pady=20
        )


