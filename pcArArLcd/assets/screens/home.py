import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from threading import Thread
import serial
import time

class home(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.user1=ImageTk.PhotoImage(Image.open(r"assets\images\User1_2B.png").resize((120,120)))
        self.user2=ImageTk.PhotoImage(Image.open(r"assets\images\user2_02.png").resize((120,120)))
        self.conficon=ImageTk.PhotoImage(Image.open(r"assets\images\conf3.png").resize((20,20)))

        self.banderaValue=tk.BooleanVar()
        self.var=tk.IntVar()

        self.init_widgets()

        #clase, home necesita los metodos de send and read.
        self.arduino=self.manager.get_arduinoConn()

        #clase, setup necesita la clase home
        self.manager.set_home(self)

    def init_widgets(self):
        ttk.Button(
            self,
            image=self.conficon,
            #text="Configuracion",
            style="Accent.TButton",
            command=lambda: self.manager.homeTosetup(),
            padding=1
        ).place(
            x=250,
            y=25
        )

        # ttk.Button(
        #     self,
        #     text="Iniciar",
        #     style="Accent.TButton"
        # ).place(
        #     x=25,
        #     y=25
        # )

        ttk.Label(
            self,
            image=self.user1
        ).place(
            x=15,
            y=120
        )

        ttk.Label(
            self,
            image=self.user2
        ).place(
            x=165,
            y=120
        )

        self.msmUser1=ttk.Label(
            self,
            text="Mensaje..."
        )
        self.msmUser1.place(
            x=15,
            y=250
        )

        self.msmUser2=ttk.Label(
            self,
            text="Mensaje..."
        )
        self.msmUser2.place(
            x=165,
            y=250
        )

        self.inTxt=ttk.Entry(
            self
        )
        self.inTxt.place(
            x=10,
            y=400
        )

        self.inTxt.bind("<Return>",lambda event: self.sendMsm())

        ttk.Button(
            self,
            text="Enviar",
            command=self.sendMsm
        ).place(
            x=180,
            y=400
        )

        # self.bandera=ttk.Checkbutton(
        #     self,
        #     text="ON",
        #     style="ToggleButton",
        #     onvalue=0,
        #     offvalue=1,
        #     variable=self.banderaValue,
        #     command=self.banderaSwitch,
        #     width=4
        # )
        # self.bandera.place(
        #     x=10,
        #     y=365
        # )

        self.chkUsers1= ttk.Radiobutton(
            self,
            variable=self.var,
            value=1,
            command=self.selectUser,
            text="2B"
        )
        self.chkUsers1.place(
            x=15,
            y=90
        )

        self.chkUsers2= ttk.Radiobutton(
            self,
            variable=self.var,
            value=2,
            command=self.selectUser,
            text="02"
        )
        self.chkUsers2.place(
            x=165,
            y=90
        )
    
    # def banderaSwitch(self):
    #     estado=self.banderaValue.get()
    #     if(estado==True):
    #         self.bandera.config(text="OFF")
    #         self.leer()
    #     else:
    #         self.bandera.config(text="ON")

    def selectUser(self):
        estado=self.var.get()

        usuarios = {
            1:"Two-B",
            2:"ZeroTwo"
        }

        print(usuarios.get(estado))


    def sendMsm(self):
        messaje=self.inTxt.get()

        self.arduino.send_port(messaje)
        print(messaje)

        self.inTxt.delete(0,tk.END)


    # def threadRead(self):
    #     newThread = Thread(
    #         target=self.leer,
    #         daemon=True)
        
    #     newThread.start()
    
    def leer(self):
        #   Esta funcion debe inicializar y al final
        #   cilicase usando after, debe tener una forma de
        #   cerrarce

        self.arduino.read_port()
        self.procesoL(self.arduino.data)
        self.book=self.msmUser1.after(100,self.leer)
    
    def procesoL(self,data):
        self.msmUser1.config(text=data[0])
        self.msmUser2.config(text=data[1])


        

