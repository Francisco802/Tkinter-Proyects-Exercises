import tkinter as tk
from tkinter import ttk
from assets.screens.home import home
from assets.screens.conexion import conexion
from assets.screens.deslizadores import deslizadores
from assets.screens.vision import vision
from assets.screens.consola import consola

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control Isobot")
        self.center_window(self,550,850)
        self.resizable(False,False)
        self.icon()
        self.carga_theme()

        container=tk.Frame(self)
        container.pack(
            side="top",
            fil=tk.BOTH,
            expand=True
        )

        container.grid_columnconfigure(0,weight=1)
        container.rowconfigure(0,weight=1)
        self.frames={}

        pantallas=(home,conexion,deslizadores,vision,consola)     #Carga de pantallas

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
        icon=tk.PhotoImage(file="assets\\images\\icon\\icon1.png")
        self.iconphoto(True,icon)
    
    def show_frame(self,container):
        frame=self.frames[container]
        frame.tkraise()    
        
#//////////////////////////////////////////////////////////////////////

    #Funciones arduinoConn Clase
    def set_arduinoConn(self,a):
        self.arduino=a
    def get_arduinoConn(self):
        return self.arduino

    #Transicion a ventanas  principal a otros
    def homeTopage(self,pag):
        pages={
            1:conexion,  #Conexion
            2:deslizadores, 
            3:consola, 
            4:vision 
        }
        if(pag in pages): self.show_frame(pages[pag])

    #Retornos a menus
    def pageTohome(self):
        self.show_frame(home)
         

