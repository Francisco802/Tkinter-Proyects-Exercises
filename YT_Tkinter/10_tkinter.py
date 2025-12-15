#Ventanas Emergentes

import tkinter as tk
from tkinter import ttk

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana general")
        self.center_window(400,500)
        self.resizable(False,False)
        #self.icon()
        self.init_widgets()
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        ttk.Button(
            self,
            text="Registrar",
            style="Accent.TButton",
            command=self.ingresarWindow,
            width=14
        ).pack(
            anchor="w",
            padx=30,
            pady=(20,10)
        )
    
    def ingresarWindow(self):
        # Crear nueva ventana
        self.ventana_ingresar = tk.Toplevel(self)
        self.ventana_ingresar.title("Segunda ventana")
        self.ventana_ingresar.geometry("200x200")
        self.ventana_ingresar.resizable(False,False)

        ttk.Label(
            self.ventana_ingresar, 
            text="Etiqueta de ejemplo"
            ).pack(
                anchor="w", 
                padx=30, 
                pady=(5, 0)
            )


win=ventana()
win.mainloop()