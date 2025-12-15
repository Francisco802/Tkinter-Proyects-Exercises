import tkinter as tk
import sqlite3 as sql
from tkinter import ttk

class botones(tk.Frame):
    def __init__(self,parent,controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.pack(padx=10,pady=10)
        self.columnconfigure((0,1,2,3,4),weight=1,uniform="a")
        self.rowconfigure(0,weight=1,uniform="a")
        self.init_widgets()
    
    def init_widgets(self):
        self.ok=ttk.Button(
            self,
            text="Aceptar",
            command=self.acept
        )
        self.ok.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )

        self.cancel=ttk.Button(
            self,
            text="Cancelar",
            command=self.cancel
        )
        self.cancel.grid(
            column=3,
            row=0,
            padx=5,
            pady=5
        )
    
    def acept(self):
        consulta = self.controlador.get_opcion()
        datos = self.controlador.get_opcion3()
        code=int(datos[0])
        title=str(datos[1])
        time=int(datos[2])
        print(f"ok, {consulta},{datos} ")

        if(consulta==1):
            ...

        if(consulta==2):
            conn=sql.connect(r"database\\animes.db")
            cursor=conn.cursor()
            instruccion=f"INSERT INTO animesList VALUES ('{code}','{title}','{time}')"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()

        if(consulta==3):
            conn=sql.connect(r"database\\animes.db")
            cursor=conn.cursor()
            instruccion=f"DELETE FROM animesList WHERE codigo='{code}'"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()

        if(consulta==4):
            conn=sql.connect(r"database\\animes.db")
            cursor=conn.cursor()
            instruccion=f"UPDATE animesList SET titulo ='{title}' WHERE codigo={code}"
            cursor.execute(instruccion)
            instruccion=f"UPDATE animesList SET duracion ='{time}' WHERE codigo={code}"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()
    
    def cancel(self):
        print("cancel")
        self.controlador.set_opcion2("cancel")

