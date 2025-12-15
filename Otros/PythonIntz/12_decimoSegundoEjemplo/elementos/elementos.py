import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.init_widgets()

    def init_widgets(self):
        ttk.Button(
            self,
            text="Buscar archivo",
            command=self.buscar
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Guardar archivo",
            command=self.guardar
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Cambiar fuente",
            command=self.fuente
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Cambiar color",
            command=self.color
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show info",
            command=lambda: self.mss(1)
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show warning",
            command=lambda: self.mss(2)
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="Show error",
            command=lambda: self.mss(3)
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askokquestion",
            command=lambda: self.mss(4)
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askokcancel",
            command=lambda: self.mss(5)
        ).pack(
            **styles.PACK
        )

        ttk.Button(
            self,
            text="askretrycancel",
            command=lambda: self.mss(6)
        ).pack(
            **styles.PACK
        )

    def buscar(self):
        fichero = FileDialog.askopenfilename(title="Abrir un fichero")
        print(fichero)

    def guardar(self):
        ruta = FileDialog.asksaveasfile(title="Guardar un fichero")
    
    def fuente(self):
        print("No hay :(")

    def color(self):
        color = ColorChooser.askcolor(title="Elige un color")
        print(color)

    def mss(self,x):
        if(x==1):
            MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

        if(x==2):
            MessageBox.showwarning("Alerta", 
            "Sección sólo para administradores.")
        if(x==3):
            MessageBox.showerror("Error", 
            "Ha ocurrido un error inesperado.")
        if(x==4):
            resultado = MessageBox.askquestion("Salir", 
            "¿Está seguro que desea salir sin guardar?")
            if(resultado=="yes"):
                print("sali si")
        
        if(x==5):
            resultado2 = MessageBox.askokcancel("Salir", 
            "¿Sobreescribir fichero actual?")
            if resultado2 == True:
                print("sali verdadero")
        
        if(x==6):
            resultado = MessageBox.askretrycancel("Reintentar",
            "No se puede conectar")
            if resultado == True:
                print("sali verdadero")


        



