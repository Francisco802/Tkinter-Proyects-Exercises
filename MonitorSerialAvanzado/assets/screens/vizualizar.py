import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class vizualizar(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager=manager
        self.ref=ImageTk.PhotoImage(Image.open(r"assets\\images\\mayuri.png").resize((75,75)))
        self.varRead=tk.BooleanVar()
        self.varRead2=tk.IntVar()

        self.init_widgets()

        self.arduino=self.manager.get_arduinoConn()

    def init_widgets(self):
        ttk.Label(
            self,
            text="Vizualizar",
            font=("Roboto",16)
        ).pack(
            pady=(20,50)
        )

        ttk.Label(
            self,
            image=self.ref
        ).place(
            x=137,
            y=350
        )

        self.lbl_txt=ttk.Label(
            self,
            text="Mensaje..."
        )
        self.lbl_txt.place(
            x=137,
            y=430
        )

        self.btn_read=ttk.Checkbutton(
            self,
            text="Iniciar",
            style="Switch",
            onvalue=0,
            offvalue=1,
            variable=self.varRead,
            command=self.switch_read,
            width=15
        )
        self.btn_read.place(
            x=25,
            y=75
        )

        ttk.Button(
            self,
            text="Borrar",
            padding=1,
            command=self.borrar
        ).place(
            x=250,
            y=75
        )

        ttk.Progressbar(
            self,
            variable=self.varRead2,
            mode="determinate",
            length=250
        ).place(
            x=50,
            y=450
        )

        #############################
        paned=ttk.Panedwindow(
            self
        )
        paned.pack(
            #expand=True,
            fill="both",
            padx=5,
            pady=(10,5)
        )

        treeFrame= ttk.Frame(paned)
        paned.add(treeFrame,weight=1)

        scrollbar = ttk.Scrollbar(treeFrame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = ttk.Treeview(treeFrame, selectmode="extended",yscrollcommand=scrollbar.set, show="tree")
        self.listbox.pack(fill="both", expand=True,padx=10) 

        scrollbar.configure(command=self.listbox.yview)
        ###########################

        ttk.Button(
            self,
            text="Regresar",
            style="Accent.TButton",
            command=lambda: self.manager.pageTohome(),
            width=15
        ).pack(
            pady=(125,10)
        )
    
    def switch_read(self):
        estado=self.varRead.get()
        if(estado==True):
            self.btn_read.config(text="Parar")
            self.leer()
        else:
            self.btn_read.config(text="Iniciar")
            self.lbl_txt.after_cancel(self.book)    

    def leer(self):
        #   Esta funcion debe inicializar y al final
        #   cilicase usando after.

        self.arduino.read_port()
        self.procesoL(self.arduino.data)
        self.book=self.lbl_txt.after(100,self.leer)
    
    def procesoL(self,data):
        self.listbox.insert("", "end", text=data[0])
        self.listbox.yview_moveto(1)        #1: parte inferior, 0: superior, 0.5: medio
        
        self.lbl_txt.config(text=data[0])
        self.varRead2.set(data[0])
    
    def borrar(self):
        self.listbox.delete(*self.listbox.get_children())


        
        

