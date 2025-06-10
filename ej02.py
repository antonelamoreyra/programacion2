## ej2 crear un programa que utilice el import random para crear un numero aleatorio entre 1 y 20, que el usuario
##ingrese un numero y le diga si es mayor o menor que el numero random

import random
print("adivine el número del 1 al 20.")
adv = random.randint(1,20)
num = -1
while num != adv:
    num = int(input("--> "))
    if adv < num:
        print("el número a adivinar es menor.")
    elif adv > num:
        print("el número a adivinar es mayor.")
    elif adv == num:
        print("adivinó :)")
