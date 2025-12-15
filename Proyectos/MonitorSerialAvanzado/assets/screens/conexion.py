import tkinter as tk
from tkinter import ttk
from assets.components.arduinoConn import serialDivice
import serial

import serial.tools
import serial.tools.list_ports

class conexion(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager

        # Conexion necesita los metodos de open and close
        self.arduino=serialDivice(self.manager)

        self.conex=tk.BooleanVar()
        self.init_widgets()
        self.listPuertos()


    def init_widgets(self):
        ttk.Label(
            self,
            text="Configuracion de conexion",
            font=("Roboto",16)
        ).pack(
            pady=(20,30)
        )

        ttk.Label(
            self,
            text="Puertos:"
        ).pack(
            padx=(0,120)
        )

        self.puertos=ttk.Combobox(
            self,
            state="readonly",
            values=[]
        )
    
        self.puertos.pack(
            pady=10
        )

        ttk.Button(
            self,
            text="Actualizar",
            command=self.listPuertos,
            style="Accent.TButton"
        ).pack(
            pady=10
        )
        
        ttk.Label(
            self,
            text="Baudrate:"
        ).pack(
            padx=(0,120)
        )

        self.velocidad=ttk.Combobox(
            self,
            state="readonly",
            values=["9600","19200","38400","57600","115200"]
        )
        self.velocidad.current(0)
        self.velocidad.pack(
            pady=10
        )

        self.habilitar=ttk.Checkbutton(
            self,
            text="Desconectado",
            style="Switch",
            onvalue=0,
            offvalue=1,
            variable=self.conex,
            command=self.conn
        )
        self.habilitar.pack(pady=10)

        ttk.Button(
            self,
            text="Regresar",
            command=lambda:self.manager.pageTohome(),
            style="Accent.TButton"
        ).pack(
            pady=10
        )
    
    def conn(self):
        estado=self.conex.get()

        if(estado==True):
            self.habilitar.config(text="Conectado")
            self.arduino.open_port(self.puertos.get(),self.velocidad.get())
            

        if(estado==False):
            self.habilitar.config(text="Desconectado")
            self.arduino.close_port()

        
    def listPuertos(self):
        listP=serial.tools.list_ports.comports()
        lista_puertos = []

        for puerto in listP:
            lista_puertos.append(puerto.device)

        if(len(lista_puertos)==0):
            lista_puertos.append("No encontrados")
            
        self.puertos.config(values=lista_puertos)
        self.puertos.current(0)

        if(self.puertos.get()!="No encontrados"): 
            self.habilitar.config(state="normal")
        else:
            self.habilitar.config(state="disable")


        

