import tkinter as tk
from tkinter import ttk
from assets.screens.home import home
from assets.screens.setup import setup

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana General")
        self.center_window(self,450,300)
        self.resizable(False,False)
        self.icon()
        self.carga_theme()
        
        container=tk.Frame(self)
        container.pack(
            side="top",
            fil=tk.BOTH,
            expand=True
        )

        container.configure(
            background="red"
        )

        container.grid_columnconfigure(0,weight=1)
        container.rowconfigure(0,weight=1)
        self.frames={}

        pantallas=(setup,home) #Carga de pantallas

        for F in pantallas:
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="NSEW")        
        
        self.show_frame(home)


    def center_window(self,window,alto,ancho):
        x = (window.winfo_screenwidth() // 2) - (ancho // 2)
        y = (window.winfo_screenheight() // 2) - (alto // 2)

        window.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    def carga_theme(self):
        #thema
        self.forest=ttk.Style(self)
        self.tk.call("source",r"assets\\theme\\Claro\\forest-light.tcl")
        self.forest.theme_use("forest-light")
    
    def icon(self):
        icon=tk.PhotoImage(file="assets\\images\\icon\\makima1.png")
        self.iconphoto(True,icon)
    
    def show_frame(self,container):
        frame=self.frames[container]
        frame.tkraise()

    # #Funcion que recibe el objeto puerto y envia a switch, SET (se establece el valor)
    # def set_objetPuerto(self,puerto):
    #     self.puerto=puerto
    # def get_objetPuerto(self):
    #     return self.puerto
    
    #Funciones arduinoConn Clase
    def set_arduinoConn(self,a):
        self.arduino=a
    def get_arduinoConn(self):
        return self.arduino
    
    #Funcion homeTosetup para iniciar la lectura
    def set_home(self,a):
        self.home_conexion=a
    def get_home(self):
        return self.home_conexion

    #Transiscion de pantalla
    def homeTosetup(self):
        self.show_frame(setup)
    
    def setupTohome(self):
        self.show_frame(home)
        

         

