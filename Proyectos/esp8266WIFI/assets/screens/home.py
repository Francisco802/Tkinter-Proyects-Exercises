import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from pyModbusTCP.client import ModbusClient # type: ignore
import time

class home(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.ref1=ImageTk.PhotoImage(Image.open(r"assets\\images\\mblue.png").resize((75,75)))
        self.ref2=ImageTk.PhotoImage(Image.open(r"assets\\images\\mred.png").resize((75,75)))
        self.varRead=tk.IntVar()
        self.varScale=tk.IntVar()
        self.conex=tk.BooleanVar()
        self.btn=tk.BooleanVar()


        self.init_widgets()

    def init_widgets(self):

        ttk.Label(
            self,
            text="ESP8266 WIFI",
            font=("Roboto",16)
        ).pack(
            pady=(20,10)
        )
        
        self.habilitar=ttk.Checkbutton(
            self,
            text="Desconectado",
            style="Switch",
            onvalue=0,
            offvalue=1,
            variable=self.conex,
            command=self.open_close_esp
        )
        self.habilitar.pack(pady=10)

        self.img=ttk.Label(
            self,
            image=self.ref1,

        )
        self.img.pack()

        ttk.Label(
            self,
            text="Deteccion pulsador" 
        ).pack(
            pady=(5,20)
        )

        self.btnon=ttk.Checkbutton(
            self,
            text="Encender Led",
            style="ToggleButton",
            onvalue=0,
            offvalue=1,
            variable=self.btn,
            command=self.on_btn
        )
        self.btnon.pack(pady=10)

        ttk.Label(
            self,
            text="Potenciometro" 
        ).pack(
            pady=(20,5)
        )

        ttk.Progressbar(
            self,
            variable=self.varRead,
            mode="determinate",
            length=250
        ).pack(
            pady=(5,20)
        )

        self.lbl_scale1=ttk.Label(
            self,
            text="Deslizador: 1, 0 To 255, x = 0" 
        )
        self.lbl_scale1.pack(
            pady=(20,5)
        )

        ttk.Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            length=180,
            variable=self.varScale,
            command=lambda event: self.sendVar(event)
        ).pack(
            pady=20
        )

        ttk.Button(
            self,
            text="Salir",
            style="Accent.TButton",
            command=self.manager.destroy,
            width=15
        ).pack(
            pady=(20,10)
        )
    

    def open_close_esp(self):
        estado=self.conex.get()

        if(estado==True):
            self.serverHost = "192.168.1.72"
            self.serverPort = 502

            self.client = ModbusClient(
                host=self.serverHost,
                port=self.serverPort,
                auto_open=True
            )
            print("Conectado...")
            self.read_esp()
        
        if(estado==False):
            self.client.close()
            self.lbl_scale1.after_cancel(self.book)  
    
    def read_esp(self):
        self.pulsador = self.client.read_discrete_inputs(0,1)
        self.potenciometro = self.client.read_input_registers(0,1)


        self.proceso()

        self.book=self.lbl_scale1.after(100,self.read_esp)

    def proceso(self):

        if(self.pulsador[0]==1):
            self.img.config(image=self.ref1)
        
        if(self.pulsador[0]==0):
            self.img.config(image=self.ref2)

        val=float(self.potenciometro[0])*(100/1024)
        self.varRead.set(val)
    
    def on_btn(self):
        estado = self.btn.get()
        if(estado==True):
            self.client.write_single_coil(0,1)

        if(estado==False):
            self.client.write_single_coil(0,0)

    def sendVar(self,event):
        txt = self.varScale.get()
        self.lbl_scale1.config(text=f"Deslizador: 1, 0 To 180, x = {txt}" )
        self.client.write_single_register(0,txt)