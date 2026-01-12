# Crear una lista con los cuadrados de los n primeros números naturales 
def cuadrados(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    return lista

def cubos(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**3)
    return lista

def main():
    print(cuadrados(10))
    print(cubos(10))

if __name__ == "__main__":
    main()
    