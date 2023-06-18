def dividir(dividendo,divisor):
    return dividendo / divisor

res = dividir(10,5)

print(res)

if __name__ == "__main__":
    try:
        dividendo = int(input("ingrese el dividendo: "))
        divisor = int(input("ingrese el divisor: "))
        res = dividir(dividendo,divisor)
        print(res)
    except ValueError:
        print("no se aceptan decimales")
    except ZeroDivisionError:
        print("no se puede dividir entre 0:")
    finally:
        print("se ha finalizado el proceso")