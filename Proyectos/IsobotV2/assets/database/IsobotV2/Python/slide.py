import tkinter as tk
from tkinter import ttk
import serial
import time

arduino = serial.Serial()

class comSerial():
    def port_open(self):
        arduino.baudrate="9600"
        arduino.port="COM4"
        arduino.open()
        time.sleep(1)

    def port_close(self):
        arduino.close()

def BD0(x):
    J0 = sld_j0.get()+128
    J0="J0"+str(J0)
    joints_BD(J0)

def BD1(x):
    J1 = sld_j1.get()+128
    J1="J1"+str(J1)
    joints_BD(J1)

def BD2(x):
    J2 = sld_j2.get()+128
    J2="J2"+str(J2)
    joints_BD(J2)

def BD3(x):
    J3 = sld_j3.get()+128
    J3="J3"+str(J3)
    joints_BD(J3)

def BD4(x):
    J4 = sld_j4.get()+128
    J4="J4"+str(J4)
    joints_BD(J4)

def joints_BD(J):
    Jt=J+"\n"
    print(J)
    arduino.write(Jt.encode("ascii"))
    time.sleep(0.1)

def seleccionar_opcion(event):
    seleccion = opciones.get()
    lbl_op.config(text=seleccion)

    if(seleccion==Vop[0]):
        CMD="$OBD\n"
    elif(seleccion==Vop[1]):
        CMD="$OBI\n"
    elif(seleccion==Vop[2]):
        CMD="$OPD\n"
    elif(seleccion==Vop[3]):
        CMD="$OPI\n"
    print(CMD)

    arduino.write(CMD.encode("ascii"))
    time.sleep(0.1)

port1=comSerial()

root=tk.Tk()

root.geometry("450x350")

#-------------------------------------------------------

gp1=tk.LabelFrame(root,text="Control (Joint))",padx=5,pady=5)
gp1.place(x=20,y=30)

gp2=tk.LabelFrame(root,text="Comunicacion Serial",padx=5,pady=5)
gp2.place(x=230,y=30)

gp3=tk.LabelFrame(root,text="Seleccion Extremidad",padx=5,pady=5)
gp3.place(x=230,y=150)

#------------------------------------------------------
lbl_j1 = tk.Label(gp1, text="Joint 1").grid(column=1,row=1)
lbl_j2 = tk.Label(gp1, text="Joint 2").grid(column=1,row=2)
lbl_j3 = tk.Label(gp1, text="Joint 3").grid(column=1,row=3)
lbl_j4 = tk.Label(gp1, text="Joint 4").grid(column=1,row=4)
lbl_j5 = tk.Label(gp1, text="Joint 5").grid(column=1,row=5)

sld_j0=tk.Scale(gp1,from_=-128,to=92,orient="horizontal",command=BD0,resolution=5)
sld_j0.grid(column=0,row=1)

sld_j1=tk.Scale(gp1,from_=-128,to=92,orient="horizontal",command=BD1,resolution=5)
sld_j1.grid(column=0,row=2)

sld_j2=tk.Scale(gp1,from_=-128,to=92,orient="horizontal",command=BD2,resolution=5)
sld_j2.grid(column=0,row=3)

sld_j3=tk.Scale(gp1,from_=-128,to=92,orient="horizontal",command=BD3,resolution=5)
sld_j3.grid(column=0,row=4)

sld_j4=tk.Scale(gp1,from_=-128,to=92,orient="horizontal",command=BD4,resolution=5)
sld_j4.grid(column=0,row=5)

#-------------------------------------------------------

btn_conect=tk.Button(gp2,text="Conectar",command=port1.port_open)
btn_conect.pack(padx=5, pady=5)

btn_close=tk.Button(gp2,text="Cerrar",command=port1.port_close)
btn_close.pack(padx=5, pady=5)

#-------------------------------------------------------
lbl_op = tk.Label(gp3, text="Eliga una opcion: ")
lbl_op.grid(column=0,row=0)

Vop=["Brazo Derecho","Brazo Izquierdo","Pierna Derecha","Pierna Izquierda"]
opciones=ttk.Combobox(gp3, values=Vop)
opciones.grid(column=0,row=1)

opciones.bind("<<ComboboxSelected>>", seleccionar_opcion)

root.mainloop()
