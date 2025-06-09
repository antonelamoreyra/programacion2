## ej9: escribir una funcion que calcule el total de una factura tras aplicarle el iva.
##la funcion debe recibir el importe sin iva y el porcentaje de iva a aplicar.
##si se invoca la funcion sin pasarle el porcentaje de iva, debera aplicar un 21%

def total(imp, iva=21):
    total= imp + imp * iva / 100
    print("total: ", total, " con el ", iva,"% de IVA")

importe= int(input("precio sin iva: "))

opc= input("sabe el % de iva a aplicar? (si/no)")
if opc.lower() == "si":
    iva= int(input("iva% -> "))
    total(importe, iva)
elif opc.lower() == "no":
    total(importe)
    
    
