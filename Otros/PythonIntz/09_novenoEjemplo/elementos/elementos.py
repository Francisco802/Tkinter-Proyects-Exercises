import tkinter as tk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.opcion1=tk.IntVar()
        self.opcion2=tk.IntVar()
        self.opcion3=tk.IntVar()
        self.init_widgets()

    def init_widgets(self):

        ##Bloque 1
        colorPelo=tk.LabelFrame(
            self,
            text="Color de pelo"
        )
        colorPelo.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        tk.Radiobutton(
            colorPelo,
            text="Rubio",
            variable=self.opcion1,
            value=1
        ).pack()

        tk.Radiobutton(
            colorPelo,
            text="Moreno",
            variable=self.opcion1,
            value=2
        ).pack()

        tk.Radiobutton(
            colorPelo,
            text="Castano",
            variable=self.opcion1,
            value=3
        ).pack()

        tk.Radiobutton(
            colorPelo,
            text="Blanco",
            variable=self.opcion1,
            value=4
        ).pack()

        #Bloque 2
        complexion=tk.LabelFrame(
            self,
            text="Complexion"
        )
        complexion.grid(
            column=0,
            row=1,
            padx=10,
            pady=10
        )

        tk.Radiobutton(
            complexion,
            text="Delgada",
            variable=self.opcion2,
            value=1
        ).pack()

        tk.Radiobutton(
            complexion,
            text="Normal",
            variable=self.opcion2,
            value=2
        ).pack()

        tk.Radiobutton(
            complexion,
            text="Gruesa",
            variable=self.opcion2,
            value=3
        ).pack()

        tk.Radiobutton(
            complexion,
            text="Muy gruesa",
            variable=self.opcion2,
            value=4
        ).pack()

        #Bloque 3
        deporteFav=tk.LabelFrame(
            self,
            text="Deporte favorito"
        )
        deporteFav.grid(
            column=0,
            row=2,
            padx=10,
            pady=10
        )

        tk.Radiobutton(
            deporteFav,
            text="Baloncesto",
            variable=self.opcion3,
            value=1
        ).pack()

        tk.Radiobutton(
            deporteFav,
            text="Futbol",
            variable=self.opcion3,
            value=2
        ).pack()

        tk.Radiobutton(
            deporteFav,
            text="Tenis",
            variable=self.opcion3,
            value=3
        ).pack()

        tk.Radiobutton(
            deporteFav,
            text="Ciclismo",
            variable=self.opcion3,
            value=4
        ).pack()

        tk.Button(
            self,
            text="Seleccionar",
            command=self.caracteristicas
        ).grid(
            column=1,
            row=1
        )

        tk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy
        ).grid(
            column=1,
            row=2
        )

        self.L1=tk.Label(
            self,
            text="Sin Caracteristicas"
        )
        self.L1.grid(
            column=1,
            row=0
        )
    
    def caracteristicas(self):
        pelo=["Rubio","Moreno","Castano","Blanco"]
        complexion=["Delgada","Normal","Gruesa","Muy gruesa"]
        deporte=["Baloncesto","Futbol","Tenis","Ciclismo"]

        stxt1=f"El color de pelo es {pelo[self.opcion1.get()-1]}.\n" 
        stxt2=f"La complexion es {complexion[self.opcion2.get()-1]}.\n"
        stxt3=f"El deporte favorito es {deporte[self.opcion3.get()-1]}."

        self.L1.config(text=stxt1+stxt2+stxt3)




