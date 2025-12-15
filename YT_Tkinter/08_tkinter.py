#ContexMenu

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
        self.menuContex=tk.Menu(self,tearoff=0)

        self.menuContex.add_command(label="Verde",command=lambda: self.LF.config(image=self.Im3))
        self.menuContex.add_command(label="Ambar",command=lambda: self.LF.config(image=self.Im2))
        self.menuContex.add_command(label="Rojo",command=lambda: self.LF.config(image=self.Im1))

        self.bind("<Button-3>",self.showMenu)

        #-------------------------------------------------------------------
        #Imagen de fondo
        self.background=tk.Label(
            self,
            #background="red"
            image=self.imGG2
        )
        self.background.place(
            x=0,
            y=0,
            relwidth = 1, 
            relheight = 1
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

    def showMenu(self,event):
        self.menuContex.post(event.x_root,event.y_root)


win=ventana()
win.mainloop()