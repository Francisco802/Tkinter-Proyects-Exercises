#MenuStrip

import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana general")
        self.center_window(400,500)
        self.resizable(False,False)
        #self.icon()

        #Imagenes
        imG=Image.open(r"imagenes\bernoRed.png").resize((200,320))
        self.Im1=ImageTk.PhotoImage(imG)

        imG=Image.open(r"imagenes\bernoYellow.png").resize((200,320))
        self.Im2=ImageTk.PhotoImage(imG)

        imG=Image.open(r"imagenes\bernoGreen.png").resize((200,320))
        self.Im3=ImageTk.PhotoImage(imG)

        #Imagenes fondo
        imG=Image.open(r"imagenes\fondo_1.jpg").resize((1250,833))
        self.imGG=ImageTk.PhotoImage(imG)

        imG=Image.open(r"imagenes\fondo_2.jpg").resize((768,768))
        self.imGG2=ImageTk.PhotoImage(imG)


        self.init_widgets()
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        #Menu principal, barra menu
        barraMenu=tk.Menu(self)
        self.config(menu=barraMenu)

        #Menu dentro de barra menu
        menuFrases=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Frases",menu=menuFrases)

        menuFrases.add_cascade(label="Saludo", command=lambda: self.L1.config(text="Hola a todos"))
        menuFrases.add_cascade(label="Despedida", command=lambda: self.L1.config(text="Hasla la vista"))
        menuFrases.add_cascade(label="Nombre de pila", command=lambda: self.L1.config(text="Mi nombre es Borja"))
        
        #Menu dentro de barra menu
        menuImagenes=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Imagenes",menu=menuImagenes)

        menuImagenes.add_cascade(label="Verde", command=lambda: self.LF.config(image=self.Im3))
        menuImagenes.add_cascade(label="Ambar", command=lambda: self.LF.config(image=self.Im2))
        menuImagenes.add_cascade(label="Rojo", command=lambda: self.LF.config(image=self.Im1))

        #Opciones no menus
        menufotoFondo=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Foto de fondo",menu=menufotoFondo)

        menufotoFondo.add_cascade(label="Imagen 1",command=lambda: self.Fondo(1))
        menufotoFondo.add_cascade(label="Imagen 2",command=lambda: self.Fondo(2))

        barraMenu.add_cascade(label="Salir",command=self.destroy)

        #-------------------------------------------------------------------
        #Imagen de fondo
        self.background=tk.Label(
            self,
            #background="red"
            image=self.imGG
        )
        self.background.place(
            x=0,
            y=0,
            relwidth = 1, 
            relheight = 1
        )
        
        #Etiqueta de texto
        self.L1=tk.Label(
            self,
            text="Texto de inicio"
        )
        self.L1.place(
            relx=0.5, 
            rely=0.05,
            anchor="center"
        )

        #Imagenes Semaforo
        self.LF=tk.Label(
            self,
            image=self.Im1
        )
        self.LF.place(
            relx=0.5, 
            rely=0.55,
            anchor="center"
        )
    
    ##Imagenes Fondo
    def Fondo(self,x):
        if(x==1):
            self.background.config(image=self.imGG)
        elif(x==2):
            self.background.config(image=self.imGG2)


win=ventana()
win.mainloop()