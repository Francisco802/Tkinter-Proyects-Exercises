import os, sys

directory=os.path.dirname(__file__)
print(directory)
#print(directory + "\imagenes\maicon.ico")

base_path=os.path.abspath(".") #tambien puede llevar __file__
print(base_path)

directory=os.path.dirname(os.path.abspath("."))
print(directory)

directory=os.path.dirname(os.path.abspath(__file__))
print(directory)

directory=os.path.realpath(".")
print(directory)






