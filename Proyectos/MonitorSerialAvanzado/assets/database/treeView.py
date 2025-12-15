import tkinter as tk
from tkinter import ttk

class TreeviewEdit(ttk.Treeview):
    def __init__(self,master,**kw):
        super().__init__(master,**kw)

        self.bind("<Double-1>",self.ondobubleClick)
    
    def ondobubleClick(self,event):
        #identificar la region donde se dio doble clic
        regionClick = self.identify_region(event.x, event.y)

        #solo nos interesa las regiones de tree y cell, no el heading o nothing
        if(regionClick not in ("tree","cell")):
            return
        #print(regionClick)

        #cual item se le dio doble clic, la columna
        column = self.identify_column(event.x)
        
        #recuperar indice, "#0" --> 0, "#0" --> -1
        column_index = int(column[1:])-1

        #identificar la fila I001
        selected_iid = self.focus()

        #identificar items
        selected_values=self.item(selected_iid)
        
        if(column == "#0"):
            selected_text = selected_values.get("text")
        else:
            selected_text = selected_values.get("values")[column_index]
            #print("Celda no disponible")
        
        #return x,y,w,h, de una celda
        column_box = self.bbox(selected_iid, column)

        entry_edit=ttk.Entry(root, width=column_box[2])
        
        #guardar el indice de la columna y el iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0,selected_text)  
        entry_edit.select_range(0, tk.END)

        entry_edit.focus()

        entry_edit.bind("<FocusOut>",self.on_focus_out)
        entry_edit.bind("<Return>",self.on_enter_pressed)

        entry_edit.place(x=column_box[0],
                        y=column_box[1],
                        w=column_box[2],
                        h=column_box[3])

        
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



if __name__=="__main__":
    root=tk.Tk()

    #Crear columnas
    columnNames=("vehicle_name","year","colour")

    treeview_vehicles=TreeviewEdit(root,column=columnNames)

    #Anadir nombre a las columnas
    treeview_vehicles.heading("#0",text="Vehicle Type")
    treeview_vehicles.heading("vehicle_name",text="Vehicle Name")
    treeview_vehicles.heading("year",text="Year")
    treeview_vehicles.heading("colour",text="Colour")

    #insertar filas
    sedanRow=treeview_vehicles.insert(parent="",
                                      index="end",
                                      text="Sedan")
                                    
    treeview_vehicles.insert(parent=sedanRow,
                             index="end",
                             values=("Nissan versa","2010","Silver"))
    
    treeview_vehicles.insert(parent=sedanRow,
                             index="end",
                             values=("Toyota","2012","Blue"))                                   

    treeview_vehicles.pack(fill="both",expand=True)


    root.mainloop()