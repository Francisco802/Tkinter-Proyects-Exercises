import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class deslizadores(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.varScale0=tk.IntVar()
        self.varScale1=tk.IntVar()
        self.varScale2=tk.IntVar()
        self.varScale3=tk.IntVar()
        self.varScale4=tk.IntVar()

        self.imG=ImageTk.PhotoImage(Image.open(r"assets\\images\\isobot.png").resize((588,425)))

        self.init_widgets()

        #Clase, swtichPage necesita los metodos de send.
        self.arduino=self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Control Manual",
            font=("Roboto",16)
        ).grid(
            row=0,
            column=0,
            padx=(20,10),
            pady=(20,10),
            sticky="nsew"
        )

        ttk.Label(
            self,
            image=self.imG
        ).grid(
            row=0,
            column=1,
            padx=(20,10),
            pady=(25,10),
            sticky="nsew",
            rowspan=4
        )    

        self.opJoin=ttk.Combobox(
            self,
            state="redonly",
            values = ["Brazo Derecho",
                      "Brazo Izquierdo",
                      "Pierna Derecha",
                      "Pierna Izquierda"]
        )
        self.opJoin.current(0)
        self.opJoin.grid(
            row=1,
            column=0,
            padx=(20,10),
            pady=(10,10),
            sticky="nsew"
        )
        self.opJoin.bind("<<ComboboxSelected>>", self.selectOpcion)

        rangos= ttk.LabelFrame(
            self,
            text="Rangos: "
        )
        rangos.grid(
            row=2,
            column=0,
            padx=(20,10),
            pady=(20,10),
            sticky="nsew"
        )

        Vmin=-128
        Vmax=92

        self.lblJ0 = ttk.Label(rangos, text="J0 = 0")
        self.lblJ0.pack()
        self.join0=ttk.Scale(
            rangos,
            from_=Vmin,
            to=Vmax,
            orient="horizontal",
            length=180,
            variable=self.varScale0,
            command=lambda e: self.sendData("J0",self.join0.get())
        )
        self.join0.pack(
            padx=(10,10),
            pady=(10,10)
        )

        self.lblJ1 = ttk.Label(rangos, text="J1 = 0")
        self.lblJ1.pack()
        self.join1=ttk.Scale(
            rangos,
            from_=Vmin,
            to=Vmax,
            orient="horizontal",
            length=180,
            variable=self.varScale1,
            command=lambda e: self.sendData("J1",self.join1.get())
        )
        self.join1.pack(
            padx=(10,10),
            pady=(10,10)
        )

        self.lblJ2 = ttk.Label(rangos, text="J2 = 0")
        self.lblJ2.pack()
        self.join2=ttk.Scale(
            rangos,
            from_=Vmin,
            to=Vmax,
            orient="horizontal",
            length=180,
            variable=self.varScale2,
            command=lambda e: self.sendData("J2",self.join2.get())
        )
        self.join2.pack(
            padx=(10,10),
            pady=(10,10)
        )

        self.lblJ3 = ttk.Label(rangos, text="J3 = 0")
        self.lblJ3.pack()
        self.join3=ttk.Scale(
            rangos,
            from_=Vmin,
            to=Vmax,
            orient="horizontal",
            length=180,
            variable=self.varScale3,
            command=lambda e: self.sendData("J3",self.join3.get())
        )
        self.join3.pack(
            padx=(10,10),
            pady=(10,10)
        )

        self.lblJ4 = ttk.Label(rangos, text="J4 = 0")
        self.lblJ4.pack()
        self.join4=ttk.Scale(
            rangos,
            from_=Vmin,
            to=Vmax,
            orient="horizontal",
            length=180,
            variable=self.varScale4,
            command=lambda e: self.sendData("J4",self.join4.get())
        )
        self.join4.pack(
            padx=(15,15),
            pady=(10,10)
        )

        ttk.Button(
            self,
            text="Regresar",
            command=lambda:self.manager.pageTohome(),
            style="Accent.TButton"
        ).grid(
            row=3,
            column=0,
            padx=(20,10),
            pady=(25,10),
            sticky="nsew"
        )

    def sendData(self,name,valor):
        Jn=int(valor)+128

        self.lblJ0.config(text=f"J0 = {int(self.join0.get())}")
        self.lblJ1.config(text=f"J1 = {int(self.join1.get())}")
        self.lblJ2.config(text=f"J2 = {int(self.join2.get())}")
        self.lblJ3.config(text=f"J3 = {int(self.join3.get())}")
        self.lblJ4.config(text=f"J4 = {int(self.join4.get())}")
        
        Data=name+str(Jn)

        try:
            self.arduino.send_port(Data)
        except:
            print(Data)
    
    
    def selectOpcion(self,e):
        n = self.opJoin.get()

        opExt={
            "Brazo Derecho":"$OBD",
            "Brazo Izquierdo":"$OBI",
            "Pierna Derecha":"$OPD",
            "Pierna Izquierda":"$OPI"
        }

        try:
            self.arduino.send_port(opExt.get(n))
        except:
            print("Sin conexion")

