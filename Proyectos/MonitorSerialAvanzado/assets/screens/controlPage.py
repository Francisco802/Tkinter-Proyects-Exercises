import tkinter as tk
from tkinter import ttk

class controlPage(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.varScale=tk.IntVar()
        self.init_widgets()

        self.arduino=self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Control Mode",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        self.lbl_scale1=ttk.Label(
            self,
            text="Deslizador: 1, 0 To 100, x = 0" 
        )
        self.lbl_scale1.place(
            x=85,
            y=95
        )

        ttk.Scale(
            self,
            from_=0,
            to=100,
            orient="horizontal",
            length=180,
            variable=self.varScale,
            command=lambda event: self.sendVar(event)
        ).place(
            x=85,
            y=120
        )

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda:self.manager.pageTocontrol(),
            width=15
        ).pack(
            pady=(375,10)
        )
    
    def sendVar(self,event):
        txt = self.varScale.get()
        self.lbl_scale1.config(text=f"Deslizador: 1, 0 To 100, x = {txt}" )
        self.arduino.send_port(str(txt))
        print(txt)

        

