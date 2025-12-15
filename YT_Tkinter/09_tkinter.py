#Cuadros de dialogo

import tkinter as tk
from tkinter import ttk

from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana general")
        self.center_window(400,500)
        self.resizable(False,False)
        #self.icon()
        self.init_widgets()
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        ttk.Button(
            self,
            text="Buscar archivo",
            command=self.buscar,
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="Guardar archivo",
            command=self.guardar,
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="Cambiar color",
            command=self.color,
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="Show info",
            command=lambda: self.mss(1),
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="Show warning",
            command=lambda: self.mss(2),
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="Show error",
            command=lambda: self.mss(3),
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="askokquestion",
            command=lambda: self.mss(4),
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="askokcancel",
            command=lambda: self.mss(5),
            width=15
        ).pack(
            pady=5
        )

        ttk.Button(
            self,
            text="askretrycancel",
            command=lambda: self.mss(6),
            width=15
        ).pack(
            pady=5
        )

    def buscar(self):
        fichero = FileDialog.askopenfilename(title="Abrir un fichero")
        print(fichero)

    def guardar(self):
        ruta = FileDialog.asksaveasfile(title="Guardar un fichero")

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


win=ventana()
win.mainloop()