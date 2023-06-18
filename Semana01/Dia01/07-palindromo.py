palabra = str(input("frase para saber si es palindromo o no: "))
palabra = palabra.lower()

pal1 = palabra.replace(" ","")

pal2 = pal1[::-1]

if(pal1 == pal2):
    print("si es palindromo")
else:
    print("no es palindromo")