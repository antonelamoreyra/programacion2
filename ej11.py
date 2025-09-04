# #  ej. 11) los estudiantes deben pasar al frente a exponer pero nadie quiere pasar primero.
# # diseñar un programa con una lista con los nombres de los estudiantes y de forma aleatoria
# # generar otra lista que indique el orden en el que deben pasar
import random
n= 1
p= 2
ap= ""
opc=1
l= []
nl=[]
msg= "anterior orden: "
msg2= "orden sorteado: "
while n!=p:
    ap= input("nombre del estudiante: ")
    l.append(ap)
    msg= msg + str(n) + ". " + ap + ", "
    opc= int(input("agregar otro estudiante? (0: no / 1: si)"))
    if opc == 1:
        n= n+1
        p= p+1
    elif opc == 0:
        p= p-1
s=len(l)
for i in range(s):
    n=random.randint(0, len(l)-1)
    ap = l[n]
    nl.append(ap)
    msg2= msg2 +str(i+1) + ". "+ ap + ", "
    del l[n]
    s= len(l)
print(msg)
print(msg2)

    