texto = str(input("texto: "))
div = int(input("divisor: "))
tam = int(len(texto))
texto.replace(" ","")
for i in range(tam):
    if(i%div==0 and i!= 0):
        print("\t")
    print(texto[i],end="")
    