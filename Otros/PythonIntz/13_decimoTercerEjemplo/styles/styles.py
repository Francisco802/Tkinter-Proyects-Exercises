import tkinter as tk

BACKGROUND="#121212"
COMPONENT="#363636"
TEXT="#84C9FB"
FONT=("Arial", 16)


STYLE = {
    #"bg":COMPONENT,
    #"fg":TEXT,
    #"font":FONT,
    "width":8, 
    "height":1
}

PACK = {
    "side":tk.TOP,
    "fill":tk.BOTH,
    "expand":True,
    "padx":22,
    "pady":11
    
}

GRID = {
    "padx":5,
    "pady":5,
}

GRID_LABEL = {
    "padx":25,
    "pady":5,
    "sticky":"ew"
}

GRID_ENTRY = {
    "padx":5,
    "pady":5,
    "sticky":"ew"
}

GRID_BUTTON = {
    "padx":5,
    "pady":5,
    "sticky":"nsew"
}