#ej 16) importar en python una imagen y almacenarla en una matriz. implementar una funcion para rotar la imagen
#preguntar al usuario si quiere rotar 90 grados hacia la izquierda o hacia la derecha o 180 grados. mostrar
#la imagen original y la rotada

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
def rotacion(grados, d= None):
    og= np.array(im)
    c, f= im.size
    if grados == 90:
        if d == "der":
            rotada= [[0] * f for _ in range(c)]
            for i in range(f):
                for j in range(c):
                    rotada[j][f - 1 - i] = og[i][j]
            return rotada
        elif d == "izq":
            rotada= [[0] * f for _ in range(c)]
            for i in range(f):
                if i == 264:
                        break
                for j in range(c):
                    rotada[c - 1 - j][i] = og[i][j]
            return rotada
    elif grados == 180:
        return [f[::-1] for f in og[::-1]]
    
            

im= Image.open("Captura.png")
plt.title("og")
plt.imshow(im)
plt.show()

g= int(input("Rotar la imagen 90 o 180 grados? "))
if g == 90:
    opc= input("izquierda o derecha? escribir izq / der. ")
    if opc == 'izq' or opc == 'der':
        plt.imshow(np.array(rotacion(g,opc)))
        plt.show()
    else:
        print("xd")
elif g == 180:
    plt.imshow(np.array(rotacion(g)))
    plt.show()
else:
    print("xd")