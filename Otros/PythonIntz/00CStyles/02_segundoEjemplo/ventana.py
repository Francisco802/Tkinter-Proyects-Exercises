import tkinter as tk
from elementos.elementos import elementos
    #carpeta -> archivo -> clase

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Check Buttons")
        self.center_window(self,400,300)
        self.resizable(False,False)

        frame=elementos(self)
        frame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
    

    def center_window(self,window,alto,ancho):
        # Obtener las dimensiones de la pantalla
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calcular la posición para centrar la ventana
        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        # Establecer la geometría de la ventana
        window.geometry(f'{ancho}x{alto}+{x}+{y}')