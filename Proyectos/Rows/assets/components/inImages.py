from PIL import Image,ImageTk
import cv2 as cv
import numpy as np
import imutils

def leer_imagenes(ruta, tamano):
    img=ImageTk.PhotoImage(Image.open(ruta).resize(tamano))
    return img






