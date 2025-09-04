# #  ej 12) implementar en python una funcion para aplicar cifrado cesar a una cadena.
# debe pasar el mensaje y el desplazamiento como parámetros.la misma funcion debe descifrar
# el mensaje si se aplica un desplazamiento negativo
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
    return cifrado

while True:
    cad = input("cadena a cifrar: ")
    des = int(input("desplazamiento: "))
    print("mensaje original: ", cad)
    print("mensaje cifrado: ", cifr(cad,des))
