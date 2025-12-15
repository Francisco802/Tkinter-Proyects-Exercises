import tkinter as tk
from tkinter import ttk
import os
from componentes.logo import logo
from componentes.datos import datos
from componentes.botones import botones
from componentes.salir import salir
from componentes.accion import accion
from controlador import Controlador
from styles import styles    

class screen(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana

        self.controlador = Controlador()

        #thema
        self.forest=ttk.Style(self.ventana)
        self.ventana.tk.call("source",r"forestTheme\forest-light.tcl")
        self.forest.theme_use("forest-light")

        #Distribucion
        self.columnconfigure(0,weight=1)
        self.rowconfigure((0,1,2,3),weight=1)

        #Contenido
        self.init_widgets()

    def init_widgets(self):
        logo(self)
        datos(self,self.controlador)
        accion(self,self.controlador)
        botones(self,self.controlador)
        salir(self,self.ventana)


        




