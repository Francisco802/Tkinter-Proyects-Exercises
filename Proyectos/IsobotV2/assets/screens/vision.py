import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from threading import Thread

from assets.components.inImages import leer_imagenes, opencv_tk

import cv2 as cv
import numpy as np
import imutils

import mediapipe as mp
import math
import time

class vision(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.startVar=tk.BooleanVar()
        self.startArd=tk.BooleanVar(value=False)
        self.d=tk.IntVar(value=1)

        self.init_widgets()

        self.arduino = self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Vision Artificial",
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

        self.flagArduino=ttk.Checkbutton(
            self,
            text="Enviar datos (Ard)",
            style="Switch",
            onvalue=0,
            offvalue=1,
            variable=self.startArd
        )
        self.flagArduino.grid(
            row=2,
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
            row=3,
            column=0,
            padx=(20,10),
            pady=(15,10),
            sticky="nsew"
        )

        opciones= ttk.LabelFrame(
            self,
            text="Opciones "
        )
        opciones.grid(
            row=4,
            column=0,
            padx=(20,10),
            pady=(15,10),
            sticky="nsew"
        )

        radio_1=ttk.Radiobutton(opciones,text="Full body",variable=self.d,value=1)
        radio_1.pack(pady=5)
        radio_2=ttk.Radiobutton(opciones,text="Right Arm",variable=self.d,value=2)
        radio_2.pack(pady=5)

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
            rowspan=7
        )  

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            width=15,
            command=lambda: self.manager.pageTohome()
        ).grid(
            row=5,
            column=0,
            padx=(20,10),
            pady=(120,0),
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

            #######################################################
            self.mp_drawing =mp.solutions.drawing_utils
            self.mp_pose=mp.solutions.pose

            self.pose = self.mp_pose.Pose(
                static_image_mode=False,
                model_complexity = 0,
                smooth_landmarks=False,
                min_detection_confidence = 0.5, 
                min_tracking_confidence = 0.5,     
            )
            #######################################################
            
            self.cap = cv.VideoCapture(cam)  #,cv.CAP_DSHOW  cap=None cuando 


            self.opCam.config(state="disable")

            self.arduino.send_port("$OBD")
            self.arduino.send_port("J0"+str(45))
            new_thread=Thread(target=self.angulos,daemon=True)
            new_thread.start()
            

        else:
            self.startbtn.config(text="Paro la captura")
            self.cap = None
            self.opCam.config(state="redonly")
        
        self.captura()
    
         
    def captura(self):
        if (self.cap is not None):
                ret,frame = self.cap.read()

                frame=cv.flip(frame,1)
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                self.height, self.width, _=frame.shape

                if (ret==True):
                    
                    self.results = self.pose.process(frame)
                    
                    imgP = self.process(frame)
                    #imgP=frame

                    #   Transformar imagen to Tkinter
                    imageToShow= imutils.resize(imgP, width=600)
                    im = Image.fromarray(imageToShow)
                    img = ImageTk.PhotoImage(image=im)

                    #   Asiganar imagen a label
                    self.videoCap.config(image=img)
                    self.videoCap.image=img
                    self.videoCap.after(1,self.captura)
                
                else:
                    self.videoCap.image = ""
                    self.cap.release()


    def process(self,frame):

        opcion=self.d.get()

        if(opcion == 1):
            self.mp_drawing.draw_landmarks(
                frame, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(128,0,255),thickness=2,circle_radius=1),
                self.mp_drawing.DrawingSpec(color=(255,255,255),thickness=2)
            )

        if(opcion==2):
            if self.results.pose_landmarks is not None:
                frame = self.brazoDerecho(frame)

        return frame

    
    def brazoDerecho(self,frame):
        self.x1=int(self.results.pose_landmarks.landmark[11].x*self.width)
        self.y1=int(self.results.pose_landmarks.landmark[11].y*self.height)
        
        self.x2=int(self.results.pose_landmarks.landmark[13].x*self.width)
        self.y2=int(self.results.pose_landmarks.landmark[13].y*self.height)
        
        self.x3=int(self.results.pose_landmarks.landmark[15].x*self.width)
        self.y3=int(self.results.pose_landmarks.landmark[15].y*self.height)

        self.angulos()
         
        cv.line(frame,(self.x1,self.y1),(self.x2,self.y2),(255,255,255),3)
        cv.line(frame,(self.x2,self.y2),(self.x3,self.y3),(255,255,255),3)
        cv.circle(frame,(self.x1,self.y1),6,(128,0,255),-1)
        cv.circle(frame,(self.x2,self.y2),6,(128,0,255),-1)
        cv.circle(frame,(self.x3,self.y3),6,(128,0,255),-1)

        return frame
    
    def angulos(self):
        ard = self.startArd.get()
        if(ard==True):

            Dy=[-self.y2+self.y1,-self.y3+self.y2]
            Dx=[self.x2-self.x1,self.x3-self.x2]

            if (Dx[0] ==0 or Dx[1]==0):
                Dx[0]=Dx[1]=1

            th1=int(math.atan(Dy[0]/Dx[0]) * 57.29)
            th2=int(math.atan(Dy[1]/Dx[1]) * 57.29)

            print(f"th1: {th1}, th2: {th2}")

            dato1="J1"+str(th1+128)
            dato2="J2"+str(th2+128)
            self.arduino.send_port(dato1)
            self.arduino.send_port(dato2)





