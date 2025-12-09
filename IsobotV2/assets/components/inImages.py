from PIL import Image,ImageTk
import cv2 as cv
import numpy as np
import imutils

def leer_imagenes(ruta, tamano):
    img=ImageTk.PhotoImage(Image.open(ruta).resize(tamano))
    return img

def opencv_tk(image,ancho):
    # Para visualizar la imagen de entrada en la GUI (tkinter)
    imageToShow= imutils.resize(image, width=ancho)
    imageToShow = cv.cvtColor(imageToShow, cv.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShow)
    img = ImageTk.PhotoImage(image=im)

    return img





