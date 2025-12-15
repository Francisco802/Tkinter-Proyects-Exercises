import tkinter as tk
from tkinter import ttk

class terminalPage(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

        self.arduino=self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Terminal Mode",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        #ListBox con ttk (treeview)

        paned=ttk.Panedwindow(
            self
        )
        paned.pack(
            #expand=True,
            fill="both",
            padx=5,
            pady=5
        )

        treeFrame= ttk.Frame(paned)
        paned.add(treeFrame,weight=1)

        scrollbar = ttk.Scrollbar(treeFrame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = ttk.Treeview(treeFrame, selectmode="extended",yscrollcommand=scrollbar.set, show="tree")
        self.listbox.pack(fill="both", expand=True,padx=10) 

        scrollbar.configure(command=self.listbox.yview)

        #Eliminar listBox
        ttk.Button(
            self,
            text="Borrar",
            command=self.borrar
        ).place(
            x=25,
            y=360
        )

        # Elementos para anadir texto y enviarlo
        self.inTxt=ttk.Entry(
            self,
            width=25
        )
        self.inTxt.place(
            x=25,
            y=410
        )

        self.inTxt.bind("<Return>",lambda event: self.sendMsm())

        ttk.Button(
            self,
            text="Enviar",
            command=self.sendMsm
        ).place(
            x=230,
            y=410
        )


        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda:self.manager.pageTocontrol(),
            width=15
        ).pack(
            pady=(125,10)
        )
        
    def sendMsm(self):
        messaje=self.inTxt.get()

        self.listbox.insert("", "end", text=messaje)

        self.arduino.send_port(messaje)
        print(messaje)

        self.inTxt.delete(0,tk.END)
    
    def borrar(self):
        self.listbox.delete(*self.listbox.get_children())

        # Tambien se puede borrar con
        # for item in self.listbox.get_children():
        #     self.listbox.delete(item)

