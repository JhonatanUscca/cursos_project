def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Probar varios casos de la función es_primo
    casos = [1, 2, 3, 4, 5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 29]
    for n in casos:
        print(f"{n} es primo? {es_primo(n)}")

if __name__ == "__main__":
    main()


