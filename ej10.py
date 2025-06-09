## ej 10: diseñar una funcion que devuelva el factorial de el numero entero
##ingresado como parámetro

def fac(num):
    a= 1
    for i in range(2, num+1):
        a= a * i
    return a

factorial= fac(int(input("num a factorizar: ")))
print(factorial)
