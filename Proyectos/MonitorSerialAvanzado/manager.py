import tkinter as tk
from tkinter import ttk
from assets.screens.homeScreen import homeScreen
from assets.screens.conexion import conexion
from assets.screens.controles import controles
from assets.screens.switchPage import switchPage
from assets.screens.vizualizar import vizualizar
from assets.screens.controlPage import controlPage
from assets.screens.terminalPage import terminalPage
from assets.screens.informacion import informacion
from assets.components.configSwitch import configSwitch


class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana General")
        self.center_window(self,550,350)
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

        pantallas=(homeScreen,conexion,controles,switchPage,vizualizar,
                   controlPage,terminalPage,configSwitch,informacion)       #Carga de pantallas

        for F in pantallas:
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="NSEW")        
        
        self.show_frame(homeScreen)

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
    
    #////////////////////////////////////////////////////////////////////////
    
    #Funciones arduinoConn Clase
    def set_arduinoConn(self,a):
        self.arduino=a
    def get_arduinoConn(self):
        return self.arduino
    
    #Funciones switchpage clase
    def set_switchpage(self,b):
        self.switchpageClass=b
    def get_switchpage(self):
        return self.switchpageClass
    
    #funcion que recibe los datos nombre del boton para lbl
    def set_nameData(self,bData):
        self.bData=bData

        #print(bData)
    def get_nameData(self):
        return self.bData 

    #funcion que recibe los datos valor del boton
    def set_valueData(self,vData):
        self.vData=vData

        #print(bData)
    def get_valueData(self):
        return self.vData 


    #Transiciones de pantalla
    #Retornos a menus
    def pageTohome(self):
        self.show_frame(homeScreen)
    
    def pageTocontrol(self):
        self.show_frame(controles)

    #Para switch
    def switchToconfig(self):
        self.show_frame(configSwitch)
    
    def configToswitch(self):
        self.show_frame(switchPage)

    #Transicion a ventanas  
    def homeTopage(self,pag):
        pages={
            1:conexion,  #Conexion
            2:controles, #Controles
            3:vizualizar, #Vizualizar
            4:informacion #informacion
        }
        if(pag in pages): self.show_frame(pages[pag])
    
    def controlTopage(self,pag):
        pages={
            1:switchPage, #switchPage
            2:controlPage, #controlPage
            3:terminalPage  #terminalPage
        }
        if(pag in pages):self.show_frame(pages[pag])



        


    
    
        


         

