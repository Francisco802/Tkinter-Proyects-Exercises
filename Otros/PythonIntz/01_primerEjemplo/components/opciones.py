import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class opciones(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.principal=parent
        #self.configure(background="red")
        self.sizeF=10
        self.init_widgets() 

    def init_widgets(self):
        self.L1=tk.Label(
            self,
            text="TEXTO DE PRUEBA",
            font=("Arial",self.sizeF)
        )
        self.L1.grid(
            column=1,
            row=0,
            columnspan=3,
            sticky="ew",
            pady=(20,10)
        )

            #Primera Columna
        ttk.Button(
            self,
            text="Rojo",
            command=lambda: self.L1.config(fg="red")
        ).grid(
            column=1,
            row=2,
            padx=10,
            pady=10
        )
    

        ttk.Button(
            self,
            text="Verde",
            command=lambda: self.L1.config(fg="green")
        ).grid(
            column=1,
            row=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Azul",
            command=lambda: self.L1.config(fg="blue")
        ).grid(
            column=1,
            row=4,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Negro",
            command=lambda: self.L1.config(fg="black")
        ).grid(
            column=1,
            row=5,
            padx=10,
            pady=10
        )
            #Segunda Columna

        ttk.Button(
            self,
            text="Arial",
            command=lambda: self.L1.config(font=("Arial", self.sizeF))
        ).grid(
            column=2,
            row=2,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Courier",
            command=lambda: self.L1.config(font=("Courier",self.sizeF))
        ).grid(
            column=2,
            row=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="+Tamano",
            command=self.Tmano_mas
        ).grid(
            column=2,
            row=4,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="-Tamano",
            command=self.Tmano_men
        ).grid(
            column=2,
            row=5,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Salir",
            command=self.principal.destroy
        ).grid(
            column=2,
            row=6,
            padx=10,
            pady=10
        )

            #Tercer Columna
        ttk.Button(
            self,
            text="Negrita",
            command=lambda: self.L1.config(font=tkFont.Font(size=self.sizeF,weight="bold"))
        ).grid(
            column=3,
            row=2,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Cursiva",
            command=lambda: self.L1.config(font=tkFont.Font(size=self.sizeF,slant="italic"))
        ).grid(
            column=3,
            row=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Subrayado",
            command=lambda: self.L1.config(font=tkFont.Font(size=self.sizeF,underline=1))
        ).grid(
            column=3,
            row=4,
            padx=10,
            pady=10
        )

        ttk.Button(
            self,
            text="Tachado",
            command=lambda: self.L1.config(font=tkFont.Font(size=self.sizeF,overstrike=1))
        ).grid(
            column=3,
            row=5,
            padx=10,
            pady=10
        )
    
    def Tmano_mas(self):
        self.sizeF=self.sizeF+1 
        self.L1.config(font=(self.L1.cget("font"),self.sizeF))

    def Tmano_men(self):
        self.sizeF=self.sizeF-1 
        self.L1.config(font=(self.L1.cget("font"),self.sizeF))

