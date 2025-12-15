import tkinter as tk
from styles import styles
from tkinter import ttk

class elementos(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.ventana=parent
        self.var1=tk.BooleanVar(value=False)
        self.var2=tk.BooleanVar(value=False)
        self.var3=tk.BooleanVar(value=False)
        self.var4=tk.BooleanVar(value=False)
        self.init_widgets()
        
    
    def init_widgets(self):
        self.L1=tk.Label(
            self,
            text="Mi ordenador no tiene nada"
        )
        self.L1.place(
            x=50,
            y=180
        )

        ttk.Button(
            self,
            text="seleccion",
            command=self.seleccion
        ).place(
            x=200,
            y=20
        )

        ttk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy
        ).place(
            x=110,
            y=300
        )

        ttk.Checkbutton(
            self,
            text="DVD-ROM",
            variable=self.var1, 
            onvalue=1, 
            offvalue=0
        ).place(
            x=25,
            y=30,
        )

        ttk.Checkbutton(
            self,
            text="Tarjeta de sonido",
            variable=self.var2, 
            onvalue=1, 
            offvalue=0
        ).place(
            x=25,
            y=60,
        )

        ttk.Checkbutton(
            self,
            text="Tarjeta de video",
            variable=self.var3, 
            onvalue=1, 
            offvalue=0
        ).place(
            x=25,
            y=90,
        )

        ttk.Checkbutton(
            self,
            text="Conexion USB",
            variable=self.var4, 
            onvalue=1, 
            offvalue=0
        ).place(
            x=25,
            y=120,
        )

    def seleccion(self):
        chk1=self.var1.get()
        chk2=self.var2.get()
        chk3=self.var3.get()
        chk4=self.var4.get()

        if chk1:
            Op1=",DVD-ROM\n"
        else:
            Op1=""

        # Op1=",DVD-ROM\n" if chk1 else ""
        # Op2=",Tarjeta de sonido\n" if chk2 else ""
        # Op3=",Tarjeta de video\n" if chk2 else ""
        # Op4=",Conexion USB" if chk2 else ""
        
        if chk2:
            Op2=",Tarjeta de sonido\n"
        else:
            Op2=""

        if chk3:
            Op3=",Tarjeta de video\n"
        else:
            Op3=""
        
        if chk4:
            Op4=",Conexion USB"
        else:
            Op4=""

        if (chk1 or chk2 or chk3 or chk4):
            Stxt=f"Mi ordenador tiene\n{Op1}{Op2}{Op3}{Op4}"
        else:
            Stxt="No hay componentes"
        
        self.L1.config(text=Stxt)
        
        