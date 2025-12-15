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
        imG=Image.open(r"imagenes\fondo_2.jpg").resize((1250,833))
        self.imGG=ImageTk.PhotoImage(imG)

        imG=Image.open(r"imagenes\save.png").resize((25,25))
        self.toolSave=ImageTk.PhotoImage(imG)

        self.init_widgets()
        
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        #toolbar
        toolbar=tk.Frame(self)
        toolbar.pack(
            side='top',
            fill='x'
        )

        tk.Button(
            toolbar,
            image=self.toolSave,
            relief='flat',
            command=lambda: self.LF.config(image=self.Im1)
        ).pack(
            side='left',
            padx=2,
            pady=2
        )

        tk.Button(
            toolbar,
            image=self.toolSave,
            relief='flat',
            command=lambda: self.LF.config(image=self.Im2)
        ).pack(
            side='left',
            padx=2,
            pady=2
        )

        tk.Button(
            toolbar,
            image=self.toolSave,
            relief='flat',
            command=lambda: self.LF.config(image=self.Im3)
        ).pack(
            side='left',
            padx=2,
            pady=2
        )

        #Imagen de fondo
        self.background=tk.Label(
            self,
            #background="red"
            image=self.imGG
        )
        self.background.pack(
        )

        #Imagenes Semaforo
        self.LF=tk.Label(
            self,
            image=self.Im1
        )
        self.LF.place(
            x=230, 
            y=220,
            anchor="center"
        )

        

win = ventana()
win.mainloop()