import tkinter as tk
from elementos.elementos import elementos

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scale - TrackBars")
        self.center_window(self,400,300)
        self.resizable(False,False)

        frame = elementos(self)
        frame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )    

    def center_window(self,window,alto,ancho):
        x = (window.winfo_screenwidth() // 2) - (ancho // 2)
        y = (window.winfo_screenheight() // 2) - (alto // 2)

        window.geometry(f'{ancho}x{alto}+{x}+{y}')

