import tkinter as tk
from styles import styles    

class elementos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana=ventana
        self.init_widgets()

    def init_widgets(self):
        self.L1=tk.Label(
            self,
            text="Se ha pulsado el boton: "
        )
        self.L1.pack(
            expand=True,
            **styles.PACK
        )

        self.ventana.bind("<Enter>", self.sss)
        self.ventana.bind("<Button-3>", lambda event: self.L1.config(text="Se ha pulsado el boton:\n Derecho del mouse"))

        #<Button-1> boton izquierdo mouse
        #<Button-2> boton central mouse
        #<Button-3> boton derecho mouse
        #<Button-1> boton izquierdo mouse

    def sss(self,event):
        self.L1.config(text="Se ha pulsado el boton:\n Izquierdo del mouse")

"""Eventos de Mouse
"<Button-1>": Botón izquierdo del mouse.
"<Button-2>": Botón central del mouse (rueda del mouse en algunos sistemas).
"<Button-3>": Botón derecho del mouse.
"<Double-Button-1>": Doble clic con el botón izquierdo del mouse.
"<Double-Button-2>": Doble clic con el botón central del mouse.
"<Double-Button-3>": Doble clic con el botón derecho del mouse.
"<Motion>": Movimiento del mouse.
"<Enter>": El cursor del mouse entra en el widget.
"<Leave>": El cursor del mouse sale del widget.
Eventos de Teclado
"<KeyPress>": Se presiona una tecla.
"<KeyRelease>": Se suelta una tecla.
"<Return>": Tecla Enter.
"<Escape>": Tecla Escape.
"<BackSpace>": Tecla de retroceso (Backspace).
"<Tab>": Tecla Tab.
"<Shift_L>": Tecla Shift izquierda.
"<Shift_R>": Tecla Shift derecha.
"<Control_L>": Tecla Control izquierda.
"<Control_R>": Tecla Control derecha.
"<Alt_L>": Tecla Alt izquierda.
"<Alt_R>": Tecla Alt derecha.
"<F1>", "<F2>", ..., "<F12>": Teclas de función F1 a F12.
"<space>": Barra espaciadora."""


