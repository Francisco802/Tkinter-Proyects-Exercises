import tkinter as tk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.val1=tk.IntVar()
        self.val2=tk.IntVar()
        self.val3=tk.IntVar()
        self.init_widgets()

    def init_widgets(self):
        tk.Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            label= "Rojo",
            variable=self.val1,
            command=lambda x: self.change_color(), #lambda x: print(self.val1.get())
            resolution=1
        ).pack(
            **styles.PACK
        )

        tk.Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            label= "Verde",
            variable=self.val2,
            command=lambda y: self.change_color(), #lambda y: print(self.val2.get())
            resolution=1
        ).pack(
            **styles.PACK
        )

        tk.Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            label= "Azul",
            variable=self.val3,
            command=lambda z: self.change_color(), #lambda z: print(self.val3.get())
            resolution=1
        ).pack(
            **styles.PACK
        )

        self.L1=tk.Label(
            self,
            background="#%02x%02x%02x"%(0,0,0)
        )
        self.L1.pack(
            **styles.PACK
        )

    def change_color(self):
        red=self.val1.get()
        green=self.val2.get()
        blue=self.val3.get()

        Color="#%02x%02x%02x"%(red,green,blue)

        self.L1.config(background=Color)





