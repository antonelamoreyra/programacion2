import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

im= Image.open("Captura.png")
im_gris= ImageOps.grayscale(im)
plt.imshow(im_gris, cmap= "grey")
plt.show()

nIm= Image.open("paint.png")
nIm_gris= ImageOps.grayscale(nIm)
M= np.array(nIm_gris)
f=64
c=64
for i in range(f):
    for j in range(c//2):
        ind= c-j-1
        aux= M[i][j]
        M[i][j]= M[i][ind]
        M[i][ind]= aux
plt.imshow(M, cmap= "grey")
plt.show()