def moda_listy(lista):
    slownik = dict()

    n = len(lista)
    for i in range(0, n):
        if lista[i] in slownik:
            slownik[lista[i]] += 1
            # slownik[lista[i]] = slownik.get(lista[i], 0) + 1
        else:
            slownik[lista[i]] = 1
    print(slownik)

    return max(slownik.values())


def main():
    lista = [1, 5, 3, 3, 2, 1, 5, 3, 1, 2, 3]
    print(moda_listy(lista))

if __name__ == "__main__":
    main()