# interfaz grafica (GUI) con TKinter
# gui son las siglas de graphical user interface, en python podemos implementarlas con la libreria TKinter.
# vemos el video de youtube de Dimas sobre interfaces graficas con TKinter. Ejercicio 18) adaptar el programa
# "adivina el numero" con interfaz gráfica, una vez probado convertirlo a un archivo ejecutable.
import tkinter as tk
from random import randint
from math import trunc
global p
p = 0
global hs
hs= 0
global adv
global k
global mult
mult = 0
k= False

app= tk.Tk()
app.geometry("600x500")
app.configure(background="#0e0204")
tk.Wm.wm_title(app, "Adivina el número.")
num = tk.IntVar(app)
st2= tk.StringVar(app)
st2.set("Adivina el número.")
punt= tk.StringVar(app)
res2= tk.StringVar(app)
res2.set("Toca el botón para generar un número")
punt.set("Puntaje: " + str(p) + ", Highscore: " + str(hs))

def texto(a, b):
    if a == "menor":
        res2.set("Menor que " + str(b))
    elif a == "mayor":
        res2.set("Mayor que " + str(b))
    elif a == "igual":
        res2.set("Felicidades, adivinaste! El número era " + str(adv) + ". \nPulsa el boton para generar otro número!")
        st2.set(": )")    
def jugar():
    global p
    global hs
    global mult
    global k
    global adv
    if k == False:
        adv = randint(1,20)
        k= True
        res2.set("Estoy pensando un número entre 1 y 20.")
        st2.set("Adivina el número.")
        mult= mult + 1
    else:
        nInput= abs(trunc(num.get()))
        if nInput == 0 or nInput > 20:
            res2.set("Entre 1 y 20.")
        else:
            if nInput > adv:
                texto("menor", nInput)
                if p - mult <= 0:
                    p = 0
                else:
                    p= p-mult
                if hs <= p:
                    hs= p
                punt.set("Puntaje: " + str(p) + ", Highscore: " + str(hs))
            elif nInput < adv:
                texto("mayor", nInput)
                if p - mult <= 0:
                    p = 0
                else:
                    p= p-mult
                if hs <= p:
                    hs= p
                punt.set("Puntaje: " + str(p) + ", Highscore: " + str(hs))
            elif nInput == adv:
                texto("igual", nInput)
                p = p + (10*mult)
                k= False
                if hs <= p:
                    hs= p
                punt.set("Puntaje: " + str(p) + ", Highscore: " + str(hs))
    
        
st=tk.Label(
    app,
    textvariable=st2,
    font= ("Fixedsys", 20),
    fg="#405c6f",
    bg="#181a1e"
    ).pack(pady=10, padx=10)
res= tk.Label(
    app,
    textvariable= res2,
    font= ("System", 18),
    fg="#f75e74",
    bg="#181a1e"
    ).pack(pady=10, padx=10)
entry= tk.Entry(app,
                 font=("System", 20),
                 justify="center",
                 fg= "#405c6f",
                 bg= "#181a1e",
                 textvariable=num
).pack(pady=2, padx=5, fill= tk.BOTH, expand=True)
pun= tk.Label(
    app,
    textvariable= punt,
    font= ("Fixedsys", 18),
    fg="#f75e74",
    bg="#181a1e"
    ).pack(pady=10, padx=10)
boton= tk.Button(app,
                 text= "Enviar",
                 font=("System", 20),
                 anchor="center",
                 activeforeground="#9aabba",
                 activebackground="#405c6f",
                 fg= "#96a3b4",
                 bg= "#181a1e",
                 height=2,
                 command= lambda: jugar()
).pack(pady=10, padx=5, expand=True, fill=tk.X)

app.mainloop()



