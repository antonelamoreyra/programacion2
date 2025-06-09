## ej 8 escribir una funcion que calcule el area de un circulo. parametro: radio.
##luego escribir otra funcion que calcule el volumen de un cilindro usando
##la primer funcion. 2do parametro: alto

from math import pi

def area(radio):
    area= pi*(radio**2)
    return area

def vol(alto, radio):
    
    vol = area(radio) * alto
    return vol

r= int(input("radio: "))
h= int(input("alto: "))

print("area: ", area(r), "volumen: ", vol(h, r))




    
