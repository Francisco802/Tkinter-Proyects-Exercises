import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()

treeview = ttk.Treeview()
treeview.pack()

item = treeview.insert("", tk.END, text="Elemento 1")
subitem = treeview.insert(item, tk.END, text="Subelemento 1")
treeview.insert(subitem, tk.END, text="Otro elemento")

ventana.mainloop()
  