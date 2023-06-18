nmro1=input("numero1: ")
nmro2=input("numero2: ")
operacion=input("elija la operación: ")
if(operacion=="suma"):
    resultado = int(nmro1) + int(nmro2)
elif(operacion=="resta"):
    resultado = int(nmro1) - int(nmro2)
elif(operacion=="multiplicacion"):
    resultado = int(nmro1) * int(nmro2)
elif(operacion=="division"):
    resultado = int(nmro1) / int(nmro2)
else:
    resultado = 0
print("el resultado es: " + str(resultado))