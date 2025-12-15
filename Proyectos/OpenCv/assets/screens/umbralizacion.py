import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from assets.components.inImages import leer_imagenes, opencv_tk

import cv2 as cv
import numpy as np
import imutils

class umbralizacion(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager

        self.varScale1=tk.IntVar()
        self.varScale2=tk.IntVar()
        
        self.Umbral_valor=6
        
        self.init_widgets()


    def init_widgets(self):
        ttk.Label(
            self,
            text="Umbralizacion",
            font=("Roboto",16),
            anchor="center"
        ).grid(
            row=0,
            column=0,
            padx=(20,10),
            pady=(20,0),
            sticky="nsew"
        )  

        ttk.Button(
            self,
            text="Cargar imagen",
            width=20,
            padding=0,
            command=self.carga_imagen
        ).grid(
            row=1,
            column=0,
            padx=(20,10),
            pady=(20,10),
            sticky="nsew"
        )

        self.img=ttk.Label(
            self,
            text="                       Carga una imagen...",
        )
        self.img.grid(
            row=0,
            column=1,
            padx=(75,20),
            pady=10,
            sticky="nsew",
            rowspan=5
        )

        tiposU= ttk.LabelFrame(
            self,
            text="Tipos: ",
            padding=(20,10) #3
        )
        tiposU.grid(
            row=2,
            column=0,
            padx=(20,10), #10,
            pady=(20,10), #15,
            sticky="nsew"
        )

        self.bin=ttk.Button(
            tiposU,
            text="Binarizada",
            width=10,
            command=lambda: self.umbralizacion(1,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.bin.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )

        self.binInv=ttk.Button(
            tiposU,
            text="BinInv",
            width=10,
            command=lambda: self.umbralizacion(2,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.binInv.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )

        self.trunc=ttk.Button(
            tiposU,
            text="Trunc",
            width=10,
            command=lambda: self.umbralizacion(3,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.trunc.grid(
            column=0,
            row=1,
            padx=5,
            pady=5
        )

        self.toz=ttk.Button(
            tiposU,
            text="Toz",
            width=10,
            command=lambda: self.umbralizacion(4,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.toz.grid(
            column=1,
            row=1,
            padx=5,
            pady=5
        )

        self.tozInv=ttk.Button(
            tiposU,
            text="TozInv",
            width=10,
            command=lambda: self.umbralizacion(5,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.tozInv.grid(
            column=2,
            row=0,
            padx=5,
            pady=5
        )

        self.orig=ttk.Button(
            tiposU,
            text="Original",
            width=10,
            command=lambda: self.umbralizacion(6,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.orig.grid(
            column=2,
            row=1,
            padx=5,
            pady=5
        )

        rangos= ttk.LabelFrame(
            self,
            text="Rangos: "
        )
        rangos.grid(
            row=3,
            column=0,
            padx=(20,10),
            pady=(20,10),
            sticky="nsew"
        )

        self.lbl_scale1=ttk.Label(
            rangos,
            text="T = 0" 
        )
        self.lbl_scale1.pack()

        self.tRango=ttk.Scale(
            rangos,
            from_=0,
            to=255,
            orient="horizontal",
            length=180,
            variable=self.varScale1,
            command=lambda e: self.umbralizacion(self.Umbral_valor,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.tRango.pack()

        self.lbl_scale2=ttk.Label(
            rangos,
            text="y = 0" 
        )
        self.lbl_scale2.pack(pady=(20,5))

        self.vConv=ttk.Scale(
            rangos,
            from_=0,
            to=255,
            orient="horizontal",
            length=180,
            variable=self.varScale2,
            command=lambda e: self.umbralizacion(self.Umbral_valor,self.varScale1.get(),self.varScale2.get()),
            state="disable"
        )
        self.vConv.pack(pady=(0,10))

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            width=15,
            command=lambda: self.manager.pageTohome()
        ).grid(
            row=4,
            column=0,
            padx=(20,10),
            pady=(50,10),
            sticky="nsew"
        )
    
    def umbralizacion(self,tip,t,y):

        self.lbl_scale1.config(text=f"T = {t}")
        self.lbl_scale2.config(text=f"y = {y}")
        
        tipoUmbral={
            1:cv.THRESH_BINARY,
            2:cv.THRESH_BINARY_INV,
            3:cv.THRESH_TRUNC,
            4:cv.THRESH_TOZERO,
            5:cv.THRESH_TOZERO_INV,
            6:"original"
        }
        self.Umbral_valor=tip
        self.tUmbral=tipoUmbral.get(tip)

        imageGray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        #imageGray = cv.cvtColor(imageGray, cv.COLOR_GRAY2BGR)

        if(self.tUmbral!="original"):
            _,imgConv=cv.threshold(imageGray,t,y,self.tUmbral)

            img = opencv_tk(imgConv,320)    #imagen de salida
        
        else:
            img=self.imgOriginal

        self.img.config(image=img)
        self.img.image=img
    

    def carga_imagen(self):

        path_image = filedialog.askopenfilename(
            filetypes=[
                ("image",".jpg"),
                ("image",".jpeg"),
                ("image",".png")
            ])
        
        if (len(path_image)>0):
            self.activacionBtn()

            #Leer imagen de entrada
            self.image=cv.imread(path_image)
            #self.image=imutils.resize(image,height=1280)

            #Para visualizar la imagen en la GUI (Conversion)
            img = opencv_tk(self.image,320)
            self.imgOriginal=img

            #Mostrar imagen en label
            self.img.config(image=img)
            self.img.image=img
    
    def activacionBtn(self):
        self.bin.config(state="normal")
        self.binInv.config(state="normal")
        self.toz.config(state="normal")
        self.tozInv.config(state="normal")
        self.trunc.config(state="normal")
        self.orig.configure(state="normal") #config y configure

        self.tRango.config(state="normal")
        self.vConv.config(state="normal")


        

