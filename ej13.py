## ej 13) declarar una matriz de 4 filas y 4 columnas con numeros enteros
##sucesivos a partir del 1 en cada celda. calcular la suma y la multiplicacion
##de los elementos de la diagonal principal y de la contradiagonal. mostrar en
##pantalla estos valores y los elementos de la matriz.

m =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
s= 0
s2= 0
mt= 1
mt2= 1
for i in range(len(m)):
    for x in range(len(m)):
        if i == x:
            s= s + m[i][x]
            mt= mt * m[i][x]
            print("(diagonal): ", m[i][x], end='.   ')            
            x= 3-i
            s2= s2 + m[i][x]
            mt2= mt2 * m[i][x]
            print("(contradiagonal): ", m[i][x])


print("suma      : ", s, end='.   ')
print("suma      : ", s2)
print("producto  : ", mt, end='. ')
print("producto  : ", mt2)
