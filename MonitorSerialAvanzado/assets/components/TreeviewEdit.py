import tkinter as tk
from tkinter import ttk

class TreeviewEdit(ttk.Treeview):
    def __init__(self,master,manager,**kw):
        super().__init__(master,**kw)
        self.manager=manager
        self.master=master
        self.bind("<Double-1>",self.ondobubleClick)
    
    def ondobubleClick(self,event):
        #identificar la region donde se dio doble clic
        regionClick = self.identify_region(event.x, event.y)

        #solo nos interesa las regiones de tree y cell, no el heading o nothing
        if(regionClick not in ("tree","cell")):
            return

        #cual item se le dio doble clic, la columna #0,#1
        column = self.identify_column(event.x)
        
        #recuperar indice, "#0" --> 0, "#0" --> -1
        column_index = int(column[1:])-1

        #identificar la fila I001
        selected_iid = self.focus()

        #identificar items, devuelve lista de elementos
        selected_values=self.item(selected_iid) 
        
        #se recupera el valor seleccionado
        selected_text = selected_values.get("values")[column_index]
        
        #return x,y,w,h, de una celda
        column_box = self.bbox(selected_iid, column)

        entry_edit=ttk.Entry(self.master, width=column_box[2])
        
        #guardar el indice de la columna y el iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0,selected_text)  
        entry_edit.select_range(0, tk.END)

        entry_edit.focus()

        entry_edit.bind("<FocusOut>",self.on_focus_out)
        entry_edit.bind("<Return>",self.on_enter_pressed)

        entry_edit.place(x=column_box[0]+50,
                        y=column_box[1]+60,
                        w=column_box[2],
                        h=column_box[3]+10)

        
    def on_focus_out(self,event):
        event.widget.destroy()
    
    def on_enter_pressed(self,event):
        new_tex = event.widget.get()

        #I002
        selected_iid = event.widget.editing_item_iid
        #-1 (tree column), 0 (first column)
        column_index = event.widget.editing_column_index

        if(column_index == -1):
            self.item(selected_iid,text=new_tex)
        else:
            current_values = self.item(selected_iid).get("values")
            current_values[column_index] = new_tex
            self.item(selected_iid, values=current_values)
        
        event.widget.destroy()

        #Almacenar datos
        self.objetSwitch()

        # Guardado y actualizacion de datos en switchPage
        switchPage=self.manager.get_switchpage()
        switchPage.upLbl()
    
    def objetSwitch(self):
        nameDta=[]
        valueDta=[]
        for i in range(1,10):
            selected_values=self.item(f"I00{i}")
            nombre = selected_values.get("values")[1]
            valor = selected_values.get("values")[2]

            valueDta.append(valor)
            nameDta.append(nombre)

        self.manager.set_nameData(nameDta)
        self.manager.set_valueData(valueDta)
