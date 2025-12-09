import tkinter as tk
from tkinter import ttk
from assets.components.inImages import leer_imagenes
import random
import time

class game(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.arriba1=leer_imagenes(r"assets\images\botones\arriba1.png",(75,75))
        self.abajo1=leer_imagenes(r"assets\images\botones\abajo1.png",(75,75))
        self.derecha1=leer_imagenes(r"assets\images\botones\derecha1.png",(75,75))
        self.izq1=leer_imagenes(r"assets\images\botones\izq1.png",(75,75))

        self.arriba2=leer_imagenes(r"assets\images\botones\arriba2.png",(75,75))
        self.abajo2=leer_imagenes(r"assets\images\botones\abajo2.png",(75,75))
        self.derecha2=leer_imagenes(r"assets\images\botones\derecha2.png",(75,75))
        self.izq2=leer_imagenes(r"assets\images\botones\izq2.png",(75,75))

        self.arriba3=leer_imagenes(r"assets\images\botones\arriba3.png",(75,75))
        self.abajo3=leer_imagenes(r"assets\images\botones\abajo3.png",(75,75))
        self.derecha3=leer_imagenes(r"assets\images\botones\derecha3.png",(75,75))
        self.izq3=leer_imagenes(r"assets\images\botones\izq3.png",(75,75))
        
        self.vacio=leer_imagenes(r"assets\images\botones\vacio.png",(75,75))

        self.base=[self.arriba1,self.abajo1,self.derecha1,self.izq1]
        self.correct=[self.arriba2,self.abajo2,self.derecha2,self.izq2]
        self.incorrect=[self.arriba3,self.abajo3,self.derecha3,self.izq3]

        self.etapa=1
        self.errores=0


        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Rows",
            font=("Roboto",16),
            anchor="center"
        ).grid(
            row=0,
            column=0, 
            padx=20,
            pady=(20,10)
        )

        ##########Botones################
        botones=ttk.Frame(
            self
        )
        botones.grid(row=1,column=0,padx=(100,100),pady=(10,10),sticky="nsew")


        self.pos_1=ttk.Label(
            botones,
            text="Imagen1",
            image=self.vacio
        )
        self.pos_1.pack(side="left",padx=10,pady=10)

        self.pos_2=ttk.Label(
            botones,
            text="Imagen1",
            image=self.vacio
        )
        self.pos_2.pack(side="left")

        self.pos_3=ttk.Label(
            botones,
            text="Imagen1",
            image=self.vacio
        )
        self.pos_3.pack(side="left")

        self.pos_4=ttk.Label(
            botones,
            text="Imagen1",
            image=self.vacio
        )
        self.pos_4.pack(side="left")

        self.pos_5=ttk.Label(
            botones,
            text="Imagen1",
            image=self.vacio
        )
        self.pos_5.pack(side="left",padx=10,pady=10)

        ##########################################################

        ttk.Button(
            self,
            text="Start",
            style="Accent.TButton",
            command=self.start
        ).place(
            x=250,
            y=200
        )

        self.sec=ttk.Label(
            self,
            text="",
            font=("Roboto",25),
            anchor="center"
        )
        self.sec.place(
            x=280,
            y=275
        )

        self.error=ttk.Label(
            self,
            text="Errores: 00",
            font=("Roboto",14),
            anchor="center"
        )
        self.error.place(
            x=250,
            y=350
        )
   
        self.manager.bind('<Up>',lambda e: self.seleccion(0))
        self.manager.bind('<Down>',lambda e: self.seleccion(1))
        self.manager.bind('<Right>',lambda e: self.seleccion(2))
        self.manager.bind('<Left>',lambda e: self.seleccion(3))
        


        ttk.Button(
            self,
            text="Regresar",
            command=self.manager.pageTohome
        ).place(
            x=250,
            y=425
        )

    def start(self):
        self.val=4
        self.timeBack()

    
    def seleccion(self,flecha):

        teclas={
            0:"arriba",
            1:"abajo",
            2:"Derecha",
            3:"Izquieda"
        }

        if(self.etapa==1):
            if(teclas.get(flecha)==teclas.get(self.n[0])):
                self.pos_1.config(image=self.correct[self.n[0]])
                Aux=2
            else:
                self.pos_1.config(image=self.incorrect[self.n[0]])
                self.errores+=1
                Aux=1

        if(self.etapa==2):
            if(teclas.get(flecha)==teclas.get(self.n[1])):
                self.pos_2.config(image=self.correct[self.n[1]])
                Aux=3
            else:
                self.pos_2.config(image=self.incorrect[self.n[1]])
                self.errores+=1
                Aux=2
        
        if(self.etapa==3):
            if(teclas.get(flecha)==teclas.get(self.n[2])):
                self.pos_3.config(image=self.correct[self.n[2]])
                Aux=4
            else:
                self.pos_3.config(image=self.incorrect[self.n[2]])
                self.errores+=1
                Aux=3
        
        if(self.etapa==4):
            if(teclas.get(flecha)==teclas.get(self.n[3])):
                self.pos_4.config(image=self.correct[self.n[3]])
                Aux=5
            else:
                self.pos_4.config(image=self.incorrect[self.n[3]])
                self.errores+=1
                Aux=4

        if(self.etapa==5):
            if(teclas.get(flecha)==teclas.get(self.n[4])):
                self.pos_5.config(image=self.correct[self.n[4]])
                Aux=1
                self.reset()
            else:
                self.pos_5.config(image=self.incorrect[self.n[4]])
                self.errores+=1
                Aux=5
        
        self.etapa=Aux
        self.error.config(text=f"Errores: {self.errores}")
    
    def timeBack(self):
        self.val-=1
        self.sec.config(text=f"0{self.val}...")
        
        if(self.val!=0):
            self.sec.after(1000,self.timeBack)
        else:
            #self.sec.after_cancel(n)
            self.sec.config(text="Go...")

            self.n=[0,0,0,0,0]
            for i in range(1,6):
                self.n[i-1] = random.randint(0,3)

            self.pos_1.config(image=self.base[self.n[0]])
            self.pos_2.config(image=self.base[self.n[1]])
            self.pos_3.config(image=self.base[self.n[2]])
            self.pos_4.config(image=self.base[self.n[3]])
            self.pos_5.config(image=self.base[self.n[4]])


    
    def reset(self):
        self.pos_1.config(image=self.vacio)
        self.pos_2.config(image=self.vacio)
        self.pos_3.config(image=self.vacio)
        self.pos_4.config(image=self.vacio)
        self.pos_5.config(image=self.vacio)

        self.start()
        





        

