#ListBox con threeview

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
        self.animes=[("Dungeon Meshi",),("Gants",),("Bersek",),("Claymore",),("Made in abyss",)]

        self.init_widgets()
        self.readList()
    
    def center_window(self,alto,ancho):
        x = (self.winfo_screenwidth()//2) - (ancho//2)
        y = (self.winfo_screenheight()//2) - (alto//2)
        self.geometry(f'{ancho}x{alto}+{x}+{y-25}')
    
    def icon(self):
        icon=tk.PhotoImage(file="icon1.png")
        self.iconphoto(True,icon)
    
    def init_widgets(self):
        self.listbox = ttk.Treeview(
            self, 
            columns=("0"),
            show=""
            )
        
        self.listbox.pack(
            fill="x",
            padx=10
            ) 
    
        self.listbox.bind("<Double-1>",self.recuperarDatos)

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
    
    def readList(self):
        #Eliminar datos
        for item in self.listbox.get_children():    #Filas ('I001', 'I002', 'I003', 'I004', 'I005')
            self.listbox.delete(item)
        
        #Recuperar nuevos datos
        datos = self.animes

        #Inserta los datos
        for dato in datos:
            self.listbox.insert(parent="",
                            index="end",
                            values=dato)

    def anadir(self):
        animeName=self.newAnime.get()
        if(len(animeName)>0):
            self.animes.append((animeName,))
            self.readList()
        
    def eliminar(self):
        self.listbox.delete(self.selected_iid)
        # Eliminarlo de la lista

    def borrarTodo(self):
        for item in self.listbox.get_children(): 
            self.listbox.delete(item)

        self.animes.clear()

    def recuperarDatos(self,event):
        # regionClick = self.listbox.identify_region(event.x, event.y)
        # if(regionClick not in ("tree","cell")):
        #     return
        
        self.selected_iid = self.listbox.focus()                 # I001

        selected_values=self.listbox.item(self.selected_iid)    # {'text': '', 'image': '', 'values': ['Claymore'], 'open': 0, 'tags': ''}
        selected_text = selected_values.get("values")           # ['Claymore']
        self.anime=selected_text[0]
        


win=ventana()
win.mainloop()