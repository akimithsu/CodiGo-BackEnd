def solucion(sentencia):
    nueva = sentencia.split()
    nueva2 = nueva[::-1]
    nueva2= ' '.join(nueva2)
    return nueva2

if __name__ == '__main__':
    sentencia = input("ingrese una oracion: ")
    resultado = solucion(sentencia)
    print(resultado)