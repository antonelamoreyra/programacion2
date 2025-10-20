#ej 16) importar en python una imagen y almacenarla en una matriz. implementar una funcion para rotar la imagen
#preguntar al usuario si quiere rotar 90 grados hacia la izquierda o hacia la derecha o 180 grados. mostrar
#la imagen original y la rotada

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
def rotacion(grados, direccion= None):
    og= np.array(im)
    f, c= im.size
    if grados == 90:
        M= np.empty((c,f))
    elif grados == 180:
        return [f[::-1] for f in im[::-1]]
    
            

im= Image.open("Captura.png")
plt.title("og")
plt.imshow(im)
plt.show()

g= int(input("Rotar la imagen 90 o 180 grados? "))
if g == 90:
    opc= input("izquierda o derecha? escribir izq / der. ")
    if opc == 'izq' or opc == 'der':
        rotacion(g, opc)
    else:
        print("xd")
elif g == 180:
    rotacion(g)
else:
    print("xd")