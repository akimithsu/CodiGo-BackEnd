mensaje = "hola mundo"

print(len(mensaje))
mensaje2= mensaje.find("a")
print(mensaje2)

mensaje3= mensaje.replace("l","b")
print(mensaje3)
print(mensaje.upper())
print(mensaje.lower())

mensaje4= mensaje[2:7]
print(mensaje4)

for letra in mensaje:
    print(letra)

mensaje5 = mensaje[:5]
print(mensaje5)

mensaje6 = mensaje[::-1]
print(mensaje6)