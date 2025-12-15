import tkinter as tk
from tkinter import ttk

class datos(tk.Frame):
    def __init__(self,parent,controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.c=tk.StringVar()
        self.tl=tk.StringVar()
        self.tm=tk.StringVar()

        self.pack(padx=10,pady=10)
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((0,1,2),weight=1)
        self.init_widgets()
    
    def init_widgets(self):
        ttk.Label(
            self,
            text="Codigo: "
        ).grid(
            column=0,
            row=0,
            sticky="w"
        )

        ttk.Label(
            self,
            text="Titulo: "
        ).grid(
            column=0,
            row=1,
            sticky="w"
        )

        ttk.Label(
            self,
            text="Duracion: (caps)"
        ).grid(
            column=0,
            row=2,
            sticky="w"
        )

        self.code=ttk.Entry(
            self,
            textvariable=self.c
        )
        self.code.grid(
            column=1,
            row=0,
            padx=10,
            pady=10
        )

        self.title=ttk.Entry(
            self,
            textvariable=self.tl
        )
        self.title.grid(
            column=1,
            row=1,
            padx=10,
            pady=10
        )

        self.time=ttk.Entry(
            self,
            textvariable=self.tm
        )
        self.time.grid(
            column=1,
            row=2,
            padx=10,
            pady=10
        )
    
        #self.bind("<Enter>", self.recuperar)
        self.c.trace_add('write', self.recuperar)
        self.tl.trace_add('write', self.recuperar)
        self.tm.trace_add('write', self.recuperar)
        

    def recuperar(self,var,index,mode): #,event
        if(len(self.code.get())>0 and len(self.title.get())>0 and len(self.time.get())>0):
            datos = [int(self.code.get()),
                    self.title.get(),
                    int(self.time.get())
                    ]
            self.controlador.set_opcion3(datos)

        
        
        
        
