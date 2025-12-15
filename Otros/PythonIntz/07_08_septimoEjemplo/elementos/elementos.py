import tkinter as tk
from tkinter import ttk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.animes=["Dungeon Meshi","Gants","Bersek","Claymore","Made in abyss"]
        self.init_widgets()

    def init_widgets(self):
        self.lst=tk.Listbox(
            self
        )
        self.lst.grid(
            column=0,
            row=0,
            rowspan=3,
            **styles.GRID
        )

        self.lst.insert(0,*self.animes)

        # self.listbox = ttk.Treeview(
        #     self, 
        #     selectmode="extended",
        #     show="tree")
        
        # self.listbox.pack(fill="both", expand=True,padx=10) 

        # self.listbox.insert("", "end", text="var")

        ttk.Button(
            self,
            text="Anadir",
            command=self.anadir
        ).grid(
            column=1,
            row=0,
            **styles.GRID
            
        )

        ttk.Button(
            self,
            text="Eliminar",
            command=self.eliminar
        ).grid(
            column=1,
            row=1,
            **styles.GRID
        )

        ttk.Button(
            self,
            text="Borrar todo",
            command=self.borrarTodo
        ).grid(
            column=1,
            row=2,
            **styles.GRID
        )

        ttk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy
        ).grid(
            column=1,
            row=3,
            **styles.GRID
        )

        tk.Label(
            self,
            text="Elemento a anadir"
        ).grid(
            column=0,
            row=3
        )

        """self.txtBox=tk.Entry(
            self,
            width=20
            #show="*",
        )
        self.txtBox.place(
            x=30,
            y=220
        )"""

        self.txtBox=ttk.Entry(
            self,
            width=20
            #show="*",
        )
        self.txtBox.place(
            x=30,
            y=220
        )

        self.cb=ttk.Combobox(
            self,
            state="readonly",
            values=self.animes
        )
        self.cb.place(
            x=30,
            y=250
        )

    def anadir(self):
        print("Dato del comboBox: "+ self.cb.get() + ", " + "Con indice: " + str(self.cb.current()))
        animeName=self.txtBox.get()
        if(len(animeName)>0):
            self.animes.append(animeName)
            self.lst.insert(tk.END,self.animes[-1])
        
    def eliminar(self):
        
        if(len(self.lst.curselection())>0):
            indice=self.lst.curselection()[0]
            self.lst.delete(indice)
            self.animes.pop(indice)

        
    def borrarTodo(self):
        
        self.lst.delete(0,len(self.animes))
        self.animes=[]




        






