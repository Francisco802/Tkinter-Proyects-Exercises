import tkinter as tk
from tkinter import ttk

from assets.components.inImages import leer_imagenes, opencv_tk

import cv2 as cv
import numpy as np
import imutils


class consola(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.startVar=tk.BooleanVar()

        self.init_widgets()
        
        #Clase, swtichPage necesita los metodos de send.
        self.arduino=self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Consola",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        #ListBox con ttk (treeview)

        paned=ttk.Panedwindow(
            self
        )
        paned.pack(
            #expand=True,
            fill="both",
            padx=150,
            pady=(5,10)
        )

        treeFrame= ttk.Frame(paned)
        paned.add(treeFrame,weight=1)

        scrollbar = ttk.Scrollbar(treeFrame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = ttk.Treeview(treeFrame, selectmode="extended",yscrollcommand=scrollbar.set, show="tree")
        self.listbox.pack(fill="both", expand=True,padx=10) 

        scrollbar.configure(command=self.listbox.yview)

        #Eliminar listBox
        ttk.Button(
            self,
            text="Borrar",
            command=self.borrar
        ).place(
            x=25,
            y=360
        )

        # Elementos para anadir texto y enviarlo
        self.inTxt=ttk.Entry(
            self,
            width=25
        )
        self.inTxt.place(
            x=25+225,
            y=410
        )

        self.inTxt.bind("<Return>",lambda event: self.sendMsm())

        ttk.Button(
            self,
            text="Enviar",
            command=self.sendMsm
        ).place(
            x=230+225,
            y=410
        )


        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda: self.manager.pageTohome(),
            width=15
        ).pack(
            pady=(125,10)
        )
        
    def sendMsm(self):
        messaje=self.inTxt.get()

        self.listbox.insert("", "end", text=messaje)
        self.listbox.yview_moveto(1)

        self.arduino.send_port(messaje)
        print(messaje)

        self.inTxt.delete(0,tk.END)
    
    def borrar(self):
        self.listbox.delete(*self.listbox.get_children())



        

