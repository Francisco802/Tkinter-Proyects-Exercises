import tkinter as tk
from tkinter import ttk

class accion(tk.Frame):
    def __init__(self,parent,controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.pack(padx=10,pady=10)
        self.columnconfigure((0,1,2,3),weight=1)
        self.rowconfigure(0,weight=1)
        self.init_widgets()
    
    def init_widgets(self):
        self.consulta=ttk.Button(
            self,
            text="Consulta",
            command=lambda: self.desactivar(1)
        )
        self.consulta.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )

        self.alta=ttk.Button(
            self,
            text="Alta",
            command=lambda:self.desactivar(2)
        )
        self.alta.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )

        self.baja=ttk.Button(
            self,
            text="Baja",
            command=lambda:self.desactivar(3)
        )
        self.baja.grid(
            column=2,
            row=0,
            padx=5,
            pady=5
        )

        self.modificacion=ttk.Button(
            self,
            text="Modificacion",
            command=lambda:self.desactivar(4)
        )
        self.modificacion.grid(
            column=3,
            row=0,
            padx=5,
            pady=5
        )
        
        self.bind("<Enter>", self.activar)

    def desactivar(self,opcion):
        self.consulta.config(state=tk.DISABLED)
        self.alta.config(state=tk.DISABLED)
        self.baja.config(state=tk.DISABLED)
        self.modificacion.config(state=tk.DISABLED)

        self.controlador.set_opcion(opcion)
    
    def activar(self,event):
        if(self.controlador.get_opcion2()=="cancel"):
            self.consulta.config(state=tk.ACTIVE)
            self.alta.config(state=tk.ACTIVE)
            self.baja.config(state=tk.ACTIVE)
            self.modificacion.config(state=tk.ACTIVE)

