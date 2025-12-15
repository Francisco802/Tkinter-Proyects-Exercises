#MatplotLib

import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana general")
        self.center_window(400,500)
        self.resizable(False,False)
        #self.icon()

        #Preconfiguraciones
        self.graficaVacia()

        self.init_widgets()
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        fondo = tk.Frame(self,bg="white")
        fondo.pack(expand=True,fill="both")

        ttk.Button(
            fondo,
            text="Generar",
            command=self.valoresGrafica
        ).pack(
            pady=20
        )

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            fondo
            ) 
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill='both', padx=20,pady=(0,0))
    
    def graficaVacia(self):
        self.fig = plt.Figure(figsize=(5, 2), dpi=80)
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.plot()
    
    def valoresGrafica(self):
        self.ax1.clear()
        vectorFechas = [0,1,2,3,4,5,6,7,8,9,10]
        vectorConsumos = [10,9,5,15,20,11,22,22,1,2,3]

        self.ax1.set_title("Consumo durante los ultimos dias", fontsize=10)
        self.ax1.set_xlabel("Fechas", fontsize=8)
        self.ax1.set_ylabel("Consumo", fontsize=8)
        self.ax1.tick_params(axis='both', labelsize=7)

        self.ax1.bar(vectorFechas, vectorConsumos, color='green', label="Consumo")
        #self.ax1.tick_params(axis='x', rotation=90)
        #self.fig.tight_layout()

        self.canvas.draw()


win=ventana()
win.mainloop()