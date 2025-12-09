import tkinter as tk
from tkinter import ttk

from assets.components.inImages import leer_imagenes, opencv_tk

import cv2 as cv
import numpy as np
import imutils


class videoCap(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.startVar=tk.BooleanVar()

        self.init_widgets()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Video Captura",
            font=("Roboto",16)
        ).grid(
            row=0,
            column=0,
            padx=(20,10),
            pady=(20,20),
            sticky="nsew"
        )  

        self.startbtn=ttk.Checkbutton(
            self,
            text="Iniciar captura",
            style="Switch",
            onvalue=0,
            offvalue=1,
            variable=self.startVar,
            command=self.startStop
        )
        self.startbtn.grid(
            row=1,
            column=0,
            padx=(20,10),
            pady=(10,10),
            sticky="nsew"
        )

        self.opCam=ttk.Combobox(
            self,
            state="redonly",
            values = ["Cam1","Cam2","Cam3"]
        )
        self.opCam.current(0)
        self.opCam.grid(
            row=2,
            column=0,
            padx=(20,10),
            pady=(10,250),
            sticky="nsew"
        )



        self.videoCap=ttk.Label(
            self,
            text="\t\t\t\tInicia Captura"
        )
        self.videoCap.grid(
            row=0,
            column=1,
            padx=(20,10),
            pady=(20,0),
            sticky="nsew",
            rowspan=4
        )  

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            width=15,
            command=lambda: self.manager.pageTohome()
        ).grid(
            row=3,
            column=0,
            padx=(20,10),
            pady=(80,0),
            sticky="nsew"
        )  

    def startStop(self):

        if(self.startVar.get()==True):
            self.startbtn.config(text="Inicio la captura")

            camOp={
                "Cam1":0,
                "Cam2":1,
                "Cam3":2
            }

            cam=camOp.get(self.opCam.get())
            self.cap = cv.VideoCapture(cam)  #,cv.CAP_DSHOW  cap=None cuando 

            self.opCam.config(state="disable")

        else:
            self.startbtn.config(text="Paro la captura")
            self.cap = None
            self.opCam.config(state="redonly")
        
        self.captura()
    
    def captura(self):

        if (self.cap is not None):
            ret,frame = self.cap.read()

            if (ret==True):

                img = opencv_tk(frame,600)

                self.videoCap.config(image=img)
                self.videoCap.image=img
                self.videoCap.after(10,self.captura)
            
            else:
                self.videoCap.image = ""
                self.cap.release()
    



        

