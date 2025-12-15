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
        tabControl = ttk.Notebook(self)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1,text="Pestana 1")
        tabControl.add(tab2,text="Pestana 2")
        tabControl.add(tab3,text="Pestana 3")
        tabControl.pack(expand=True,fill='both')

        tk.Label(
            tab1,
            text="Hola a todos"
        ).pack()

        tk.Label(
            tab2,
            text="meisho doto desu"
        ).pack()

        tk.Label(
            tab3,
            text="Test 2"
        ).pack()

        ttk.Button(
            self,
            text="Salir",
            command=self.destroy
        ).pack(
            padx=20,
            pady=20
        )
        

win = ventana()
win.mainloop()