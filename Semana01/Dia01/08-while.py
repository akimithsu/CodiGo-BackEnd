resultado = 0
continuar = "si"
while(continuar == "si"):
    numero = int(input("ingrese un numero: "))
    resultado +=numero
    continuar = input("desea ingresar mas numeros ? : ")
    if(continuar=="no"):
        break
print(resultado)