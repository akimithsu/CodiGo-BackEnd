lado = int(input("ingresar lado: "))
for i in range (lado):
    if(i == 0 or i == (lado-1)):
        print("* " * lado)
    else:
        print("*"+ "  " *(lado-2) + " *")
