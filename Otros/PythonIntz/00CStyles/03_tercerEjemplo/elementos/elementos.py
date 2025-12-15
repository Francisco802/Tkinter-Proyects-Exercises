import tkinter as tk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.opcion=tk.IntVar()
        self.init_widgets()

    def init_widgets(self):
        self.L1=tk.Label(
            self,
            text="Mi aparato de entretenimiento favorito es:\n"
        )
        self.L1.place(
            x=20,
            y=200
        )

        tk.Button(
            self,
            text="Seleccionar",
            command=self.verification,
            **styles.STYLE
        ).place(
            x=200,
            y=50
        )

        tk.Button(
            self,
            text="Salir",
            command=lambda:self.ventana.destroy(),
            **styles.STYLE
        ).place(
            x=120,
            y=350
        )

        tk.Radiobutton(
            self,
            text="Movil",
            variable=self.opcion,
            value=1,
            command=lambda: print("Aqui podria ir una funcion")
        ).place(
            x=20,
            y=20
        )

        tk.Radiobutton(
            self,
            text="Ordenador",
            variable=self.opcion,
            value=2
        ).place(
            x=20,
            y=50
        )

        tk.Radiobutton(
            self,
            text="Tablet",
            variable=self.opcion,
            value=3
        ).place(
            x=20,
            y=80
        )

        tk.Radiobutton(
            self,
            text="Television",
            variable=self.opcion,
            value=4
        ).place(
            x=20,
            y=110
        )

    def verification(self):
        str=""

        if(self.opcion.get()==1):
            str="Movil"
        elif(self.opcion.get()==2):
            str="Ordenador"
        elif(self.opcion.get()==3):
            str="Tablet"
        elif(self.opcion.get()==4):
            str="Television"
        else:
            pass

        
        self.L1.config(text = "Mi aparato de entretenimiento favorito es:\n"+ str)




