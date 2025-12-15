import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import serial
import time

class switchPage(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        imG=Image.open(r"assets\\images\\botonIcon2.png").resize((70,70))
        self.ImGG=ImageTk.PhotoImage(imG)
        self.init_widgets()

        #Clase, swtichPage necesita los metodos de send and read.
        self.arduino=self.manager.get_arduinoConn()

        #clase, configSwtich (treeV) necesita la clase switchpage
        self.manager.set_switchpage(self)

        #Primera carga #Funcion set_nameData y valueData
        bData=["Boton 1","Boton 2","Boton 3",
                   "Boton 4","Boton 5","Boton 6",
                    "Boton 7","Boton 8","Boton 9"] 
        vData=["1","2","3","4","5","6","7","8","9"]
        
        self.manager.set_nameData(bData)
        self.manager.set_valueData(vData)

    def init_widgets(self):
        ttk.Label(
            self,
            text="Switch Mode",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )
        

        By=90
        Ly=70
        n=0
        self.lbls=[] #revisar

        for i in range(1,10):
            self.lbls.append(ttk.Label(self,text=f"Boton {i}"))

        for i in range(3):
            Bx=30
            for j in range(3):
                n+=1
                self.lbls[n-1].place(x=Bx,y=Ly)
                ttk.Button(
                    self,
                    style="Accent.TButton",
                    command=lambda n1=n :self.sendData(n1),
                    image=self.ImGG,
                    padding=2
                ).place(x=Bx,y=By)

                Bx=Bx+105

            By+=120
            Ly+=120

        ttk.Button(
            self,
            text="Regreso",
            style="Accent.TButton",
            command=lambda:self.manager.pageTocontrol(),
            width=15
        ).pack(
            pady=(5,30),
            side="bottom"
        )

        ttk.Button(
            self,
            text="Configuracion",
            #style="Accent.TButton",
            command=lambda:self.manager.switchToconfig(),
            width=15
        ).pack(
            pady=(5,5),
            side="bottom"
        )
        
    def upLbl(self):
        # Edita los nombres de los botones
        bData=self.manager.get_nameData()
            
        for i in range(9):
            (self.lbls[i]).config(text=bData[i])
            #print(bData[i])
          
    def sendData(self,btn):
        vData=self.manager.get_valueData()
        btnValor={
            1:vData[0],
            2:vData[1],
            3:vData[2],
            4:vData[3],
            5:vData[4],
            6:vData[5],
            7:vData[6],
            8:vData[7],
            9:vData[8],
        }
        
        messaje=btnValor.get(btn)
        self.arduino.send_port(messaje)
        print(messaje)
