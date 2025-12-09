import tkinter as tk
from tkinter import ttk
from assets.components.TreeviewEdit import TreeviewEdit

class configSwitch(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()
        

    def init_widgets(self):
        ttk.Label(
            self,
            text="Asignar valores",
            font=("Roboto",16)
        ).pack(
            pady=(20,10)
        )

        #Crear columnas
        btnConfig=TreeviewEdit(self,self.manager,columns=("0","1","2"),show='headings')

        #Anadir nombre a las columnas
        btnConfig.heading("0",text="No.")
        btnConfig.heading("1",text="Boton")
        btnConfig.heading("2",text="Valor")
        btnConfig.column("0",width=20,anchor="center")
        btnConfig.column("1",width=80,anchor="center")
        btnConfig.column("2",width=80,anchor="center")

        #insertar filas
        for i in range(1,10):
            btnConfig.insert(parent="",
                                index="end",
                                values=(i,f"Boton {i}"," None"))
            
        btnConfig.pack(fill="both",
                       expand=True,
                       padx=50,
                       pady=(10,50))


        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda:self.manager.configToswitch(),
            width=15
        ).pack(
            pady=(50,50)
        )


        

