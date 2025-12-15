import tkinter as tk
from PIL import Image, ImageTk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana

        #Imagenes
        self.Im1=tk.PhotoImage(file=r"00AImagenes\RojoP.png")
        self.Im2=tk.PhotoImage(file=r"00AImagenes\AmbarP.png")
        self.Im3=tk.PhotoImage(file=r"00AImagenes\VerdeP.png")

        #Imagenes fondo
        imG=Image.open(r"00AImagenes\fondoverde.jpg").resize((1250,833))
        self.imGG=ImageTk.PhotoImage(imG)

        imG=Image.open(r"00AImagenes\LogoT1.png").resize((768,768))
        self.imGG2=ImageTk.PhotoImage(imG)

        imG=Image.open(r"00AImagenes\save.png").resize((25,25))
        self.toolSave=ImageTk.PhotoImage(imG)


        self.init_widgets()

    def init_widgets(self):
        #Menu principal, barra menu
        barraMenu=tk.Menu(self)
        self.ventana.config(menu=barraMenu)

        #Menu dentro de barra menu
        menuFrases=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Frases",menu=menuFrases)

        menuFrases.add_cascade(label="Saludo", command=lambda: self.L1.config(text="Hola a todos"))
        menuFrases.add_cascade(label="Despedida", command=lambda: self.L1.config(text="Hasla la vista"))
        menuFrases.add_cascade(label="Nombre de pila", command=lambda: self.L1.config(text="Mi nombre es Borja"))
        
        #Menu dentro de barra menu
        menuImagenes=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Imagenes",menu=menuImagenes)

        menuImagenes.add_cascade(label="Verde", command=lambda: self.LF.config(image=self.Im3))
        menuImagenes.add_cascade(label="Ambar", command=lambda: self.LF.config(image=self.Im2))
        menuImagenes.add_cascade(label="Rojo", command=lambda: self.LF.config(image=self.Im1))

        #Opciones no menus
        menufotoFondo=tk.Menu(barraMenu,tearoff=0)
        barraMenu.add_cascade(label="Foto de fondo",menu=menufotoFondo)

        menufotoFondo.add_cascade(label="Imagen 1",command=lambda: self.Fondo(1))
        menufotoFondo.add_cascade(label="Imagen 2",command=lambda: self.Fondo(2))

        barraMenu.add_cascade(label="Salir",command=self.ventana.destroy)

        #Imagen de fondo
        self.background=tk.Label(
            self,
            #background="red"
            image=self.imGG
        )
        self.background.place(
            x=0,
            y=0,
            relwidth = 1, 
            relheight = 1
        )
        
        #Etiqueta de texto
        self.L1=tk.Label(
            self,
            text="Texto de inicio"
        )
        self.L1.place(
            relx=0.5, 
            rely=0.05,
            anchor="center"
        )

        #Imagenes Semaforo
        self.LF=tk.Label(
            self,
            image=self.Im1
        )
        self.LF.place(
            relx=0.5, 
            rely=0.55,
            anchor="center"
        )

        #toolBar
        toolbar=tk.Frame(
            self.ventana,
            bd=1,
            relief="raised"
        )
        toolbar.pack(
            side=tk.TOP, 
            fill=tk.X)

        tk.Button(
            toolbar,
            image=self.toolSave,
            relief=tk.FLAT
        ).pack(
            side=tk.LEFT,
            padx=2,
            pady=2
        )

        tk.Button(
            toolbar,
            image=self.toolSave,
            relief=tk.FLAT
        ).pack(
            side=tk.LEFT,
            padx=2,
            pady=2
        )

        self.menuContex=tk.Menu(self.ventana,tearoff=0)

        self.menuContex.add_command(label="Verde",command=lambda: self.LF.config(image=self.Im3))
        self.menuContex.add_command(label="Ambar",command=lambda: self.LF.config(image=self.Im2))
        self.menuContex.add_command(label="Rojo",command=lambda: self.LF.config(image=self.Im1))

        self.ventana.bind("<Button-3>",self.showMenu)

        
    ##Imagenes Fondo
    def Fondo(self,x):
        if(x==1):
            self.background.config(image=self.imGG)
        elif(x==2):
            self.background.config(image=self.imGG2)

    def showMenu(self,event):
        self.menuContex.post(event.x_root,event.y_root)


    
    

       











