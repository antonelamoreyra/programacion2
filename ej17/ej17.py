# ej 17 aplicar un filtro de desenfoquue gaussiano a una imagen. mostrar la imagen original
# y la filtrada. kernel=[[1,2,1][2,4,2][1,2,1]]

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

ker = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]], dtype=np.float32)
ker= ker/ker.sum()

def gau(imagen):
    M= np.array(imagen, dtype=np.float32)
    f, c, r= M.shape
    gauss= M
    for ch in range(r):
        for i in range(1,f-1):
            for j in range(1,c-1):
                
                
                reg= gauss[i-1:i+2, j-1:j+2, ch]
                
                gauss[i, j, ch] = np.sum(reg * ker)
    gauss = np.clip(gauss, 0, 255)
    return Image.fromarray(gauss.astype(np.uint8))

im= Image.open("paint.png")
plt.title("og")
plt.imshow(im)
plt.show()
plt.title("desenfocado")
plt.imshow(gau(im))
plt.show()