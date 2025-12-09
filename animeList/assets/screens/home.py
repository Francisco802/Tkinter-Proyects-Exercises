import tkinter as tk
from tkinter import ttk
from assets.database.sqll import dataBse
import random

class home(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.sAccion=""
        self.db=dataBse()

        self.init_widgets()
        self.activarAcciones()

    def init_widgets(self):
        ttk.Label(
            self,
            text="AnimeList",
            font=("Roboto",16)
        ).pack(
            pady=(20,20)
        )

        xlbl=120
        ylbl=90

        ttk.Label(
            self,
            text="Codigo: "
        ).place(
            x=xlbl,
            y=ylbl
        )    
        ttk.Label(
            self,
            text="Auto para Alta. "
        ).place(
            x=xlbl+235,
            y=ylbl
        )  
        ttk.Label(
            self,
            text="Titulo: "
        ).place(
            x=xlbl,
            y=ylbl+40
        )    
        ttk.Label(
            self,
            text="Duracion: "
        ).place(
            x=xlbl,
            y=ylbl+80
        )
        ttk.Label(
            self,
            text="Caps. "
        ).place(
            x=xlbl+235,
            y=ylbl+85
        )  


        self.EntryCode=ttk.Entry(
            self
        )
        self.EntryCode.place(
            x=xlbl+70,
            y=ylbl-5
        )  
        
        self.EntryTitle=ttk.Entry(
            self
        )
        self.EntryTitle.place(
            x=xlbl+70,
            y=ylbl+35
        ) 

        self.Entrydura=ttk.Entry(
            self
        )
        self.Entrydura.place(
            x=xlbl+70,
            y=ylbl+75
        ) 


        xbtn=25  
        ybtn=ylbl+90       #90, 165

        self.btnConsulta=ttk.Button(
            self,
            text="Consulta",
            command=self.clicConsulta
        )
        self.btnConsulta.place(
            x=xbtn,
            y=ybtn+50
        ) 

        self.btnAlta=ttk.Button(
            self,
            text="Alta",
            command=self.clicAlta
        )
        self.btnAlta.place(
            x=xbtn+120,
            y=ybtn+50
        ) 

        self.btnBaja=ttk.Button(
            self,
            text="Baja",
            command=self.clicBaja
        )
        self.btnBaja.place(
            x=xbtn+240,
            y=ybtn+50,
        ) 

        self.btnMod=ttk.Button(
            self,
            text="Modificacion",
            command=self.clicModificacion
        )
        self.btnMod.place(
            x=xbtn+360,
            y=ybtn+50
        ) 


        self.btnAcept=ttk.Button(
            self,
            text="Aceptar",
            width=15,
            command=self.clicAceptar
        )
        self.btnAcept.place(
            x=xbtn+85,
            y=ybtn+115
        ) 

        self.btnCancel=ttk.Button(
            self,
            text="Cancelar",
            width=15,
            command=self.clicCancelar
        )
        self.btnCancel.place(
            x=xbtn+240,
            y=ybtn+115
        ) 

        ttk.Button(
            self,
            text="Salir",
            style="Accent.TButton",
            command=self.manager.destroy
        ).place(
            x=205,
            y=ybtn+200
        ) 

    def desactivarAcciones(self):
        self.btnConsulta.config(state="disable")
        self.btnAlta.config(state="disable")
        self.btnBaja.config(state="disable")
        self.btnMod.config(state="disable")
        self.btnCancel.config(state="normal")
        self.btnAcept.config(state="normal")

    def activarAcciones(self):
        self.btnConsulta.config(state="normal")
        self.btnAlta.config(state="normal")
        self.btnBaja.config(state="normal")
        self.btnMod.config(state="normal")
        self.btnCancel.config(state="disable")
        self.btnAcept.config(state="disable")

        self.sAccion=""

    def clicConsulta(self):
        self.sAccion="consulta"
        self.desactivarAcciones()

    def clicAlta(self):
        self.newCode = random.randint(1000, 10000)
        self.EntryCode.delete(0,"end")
        self.EntryCode.insert(0,f"{self.newCode}")

        self.sAccion="alta"
        self.desactivarAcciones()

    def clicBaja(self):
        self.sAccion="baja"
        self.desactivarAcciones()

    def clicModificacion(self):
        self.sAccion="modificacion"
        self.desactivarAcciones()

    def clicCancelar(self):
        self.activarAcciones()

    def clicAceptar(self):
        peticion=self.sAccion
        code=self.EntryCode.get()
        title = self.EntryTitle.get()
        caps = self.Entrydura.get()

        if(peticion=="consulta"):
            datos = self.db.search(int(code))
            #print(datos)
            #print(datos[0])
            row=[0,"title",0]
            val=0
            for i in datos[0]:
                row[val]=i
                val+=1
            
            self.resetEntry()

            code = row[0]
            title = row[1]
            caps = row[2]

            self.EntryCode.insert(0,code)
            self.EntryTitle.insert(0,title)
            self.Entrydura.insert(0,caps)
            

        if(peticion=="alta"):
            code=self.newCode
            self.db.insertRow(int(code),str(title),int(caps))
            self.resetEntry()

        if(peticion=="baja"):
            self.db.delate(code)
            self.resetEntry()
            

        if(peticion=="modificacion"):
            self.db.updateFields(int(code),int(caps))
            self.resetEntry()


    def resetEntry(self):
        self.EntryCode.delete(0,"end")
        self.EntryTitle.delete(0,"end")
        self.Entrydura.delete(0,"end")
