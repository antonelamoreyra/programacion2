from tkinter import ttk
import tkinter as tk

app= tk.Tk()
app.geometry("1000x600")
app.configure(background="#0e0204")
tk.Wm.wm_title(app, "Cifrado Cesar")

eMsg = tk.StringVar(app)
mCif= tk.StringVar(app)
eDes = tk.IntVar(app)

def cifr(msg, dpz):
    ev= list(msg)
    out= []
    ap= ""
    chars= list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    chars2= list("abcdefghijklmnopqrstuvwxyz")
    cifrado=""
    for i in ev:
        for x in chars:
            if i == x:
                if dpz <= 0:
                    if ord(i)-abs(dpz) <= ord("A"):
                        ap2 = ord(i)
                        count = 0
                        while ap2 >= ord("A") and count >= dpz:
                            if count == dpz:
                                break
                            if ap2 == ord("A") and count > dpz:
                                ap2 = ord("Z")
                            else:
                                ap2 = ap2 - 1
                            count = count - 1
                        out.append(chr(ap2))                    
                    else:
                        ap2= ord(i)
                        ap2= ap2 - abs(dpz)
                        out.append(chr(ap2))
                else:
                    if ord(i)+dpz >= ord("Z"):
                        ap2= ord(i)
                        count= 0
                        while ap2 <= ord("Z") and count <= dpz:
                            if count == dpz:
                                break
                            if ap2 == ord("Z") and count < dpz:
                                ap2 = ord("A")
                            else:
                                ap2= ap2 + 1
                            count= count + 1
                        out.append(chr(ap2))                   
                    else:
                        ap2= ord(i)
                        ap2= ap2 + dpz
                        out.append(chr(ap2))
        for x in chars2:
            if i == x:
                if dpz <= 0:
                    if ord(i)-abs(dpz) <= ord("a"):
                        ap2 = ord(i)
                        count = 0
                        while ap2 >= ord("a") and count >= dpz:
                            if count == dpz:
                                break
                            if ap2 == ord("a") and count > dpz:
                                ap2 = ord("z")
                            else:
                                ap2 = ap2 - 1
                            count = count - 1
                        out.append(chr(ap2))
                    else:
                        ap2= ord(i)
                        ap2= ap2 - abs(dpz)
                        out.append(chr(ap2))
                else:
                    if ord(i)+dpz > ord("z"):
                        ap2 = ord(i)
                        count= 0
                        while ap2 <= ord("z") and count <= dpz:
                            if count == dpz:
                                break
                            if ap2 == ord("z") and count < dpz:
                                ap2 = ord("a")
                            else:
                                ap2= ap2 + 1
                            count= count + 1
                        out.append(chr(ap2))
                    else:
                        ap2 = ord(i)
                        ap2 = ap2 + dpz
                        out.append(chr(ap2))
        if not i in chars and not i in chars2:
            out.append(i)
    for z in out:
        cifrado= cifrado + z
    mCif.set(cifrado)

t=tk.Label(
    app,
    text= "Cifra o descifra un texto aquí. :)",
    font= ("System", 20),
    fg="#f75e74",
    bg="#181a1e")
t.place(x=1000/6, y=70)
entry= tk.Entry(app,
                 font=("System", 50),
                 justify="center",
                 fg= "#405c6f",
                 bg= "#181a1e",
                 textvariable=eMsg,
                 width= 15)
entry.place(x=1000/5,y=150)
des= tk.Label(
    app,
    text= "Desplazamiento:",
    font= ("Fixedsys", 15),
    anchor="center",
    fg="#f75e74",
    bg="#181a1e",
    height= 2
    )
des.place(x=1000/5,y=300)
des2= tk.Entry(app,
                 font=("System", 18),
                 justify="center",
                 fg= "#405c6f",
                 bg= "#181a1e",
                 textvariable=eDes,
                 width= 5
)
des2.place(x=(1000/6*2),y=300)
env= tk.Button(app,
                 text= "Cifrar/Descifrar",
                 font=("System", 18),
                 anchor="center",
                 activeforeground="#9aabba",
                 activebackground="#405c6f",
                 fg= "#96a3b4",
                 bg= "#181a1e",
                 command= lambda: cifr(eMsg.get(), eDes.get()))
env.place(x=1000/6*3,y=290)
tRes= tk.Label(
    app,
    text="tu texto dice:",
    font= ("System", 26),
    fg="#f75e74",
    bg="#181a1e"
    )
tRes.place(x=1000/5,y=400)
res= tk.Label(
    app,
    justify="center",
    textvariable= mCif,
    wraplength=800,
    font= ("System", 30),
    fg="#f75e74",
    bg="#181a1e")
res.place(x=1000/8,y=450)

##cad = input("cadena a cifrar: ")
##des = int(input("desplazamiento: "))
##print("mensaje original: ", cad)
##print("mensaje cifrado: ", cifr(cad,des))

app.mainloop()