#ListBox basico

import tkinter as tk
from tkinter import ttk

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana general")
        self.center_window(400,500)
        self.resizable(False,False)
        #self.icon()

        #variables
        self.animes=["Dungeon Meshi","Gants","Bersek","Claymore","Made in abyss"]

        self.init_widgets()
        
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        self.lst=tk.Listbox(
            self,
            selectmode="single"
        )
        self.lst.pack(
            fill="x"
        )

        self.lst.insert(0,*self.animes)

        ttk.Button(
            self,
            text="Anadir",
            command=self.anadir
        ).pack(
            pady=2,
            fill="x"
        )

        ttk.Button(
            self,
            text="Eliminar",
            command=self.eliminar
        ).pack(
            pady=2,
            fill="x"
        )

        ttk.Button(
            self,
            text="Borrar todo",
            command=self.borrarTodo
        ).pack(
            pady=2,
            fill="x"
        )

        ttk.Button(
            self,
            text="Salir",
            command=self.destroy
        ).pack(
            pady=2,
            fill="x"
        )

        tk.Label(
            self,
            text="Elemento a anadir"
        ).pack(
            pady=(10,2),
            fill="x"
        )

        self.newAnime=ttk.Entry(
            self,
            width=20
        )
        self.newAnime.pack(
            pady=2,
            fill="x"
        )

    def anadir(self):
        animeName=self.newAnime.get()
        if(len(animeName)>0):
            self.animes.append(animeName)
            self.lst.insert("end",animeName)
        
    def eliminar(self):
        indice=self.lst.curselection()[0]
        self.lst.delete(indice)
        self.animes.pop(indice)
 
    def borrarTodo(self):
        self.lst.delete(0,'end')
        self.animes.clear()


win=ventana()
win.mainloop()