# ej15)importar en python una imagen a color y mostrarla. definir una funcion para convertir imágenes
#a escala de grises y mostrar el resutado. no se deben usar funciones integradas. en su lugar usar
#la fórmula: gris= R*0.2989+G*0.5870+B*0.1140

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
global f
global c
f= 64
c= 64
def gris(im):
    M= np.array(im)
    for i in range(f):
        for j in range(c):
            r= M[i][j][0]
            g= M[i][j][1]
            b= M[i][j][2]
            gris= r*0.2989+g*0.5870+b*0.1140
            M[i][j][0]= gris
            M[i][j][1]= gris
            M[i][j][2]= gris
            
    return M
im= Image.open("paint.png")
plt.imshow(im)
plt.title("normal")
plt.show()
im_gris= gris(im)
plt.title("escala de grises")
plt.imshow(im_gris)
plt.show()