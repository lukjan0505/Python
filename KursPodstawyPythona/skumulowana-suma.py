lista = [1, 2, 4, 6, 9]

def skumulowana_suma(lista):
    wynik = [None] * len(lista)
    poprzedni = 0
    for index, element in enumerate(lista):
        wynik[index] = poprzedni + element
        poprzedni = wynik[index]
    return wynik


# dla liczb 1,3,6,8, skumulowana suma, to 1, 4, 10, 18
def main():
    print(skumulowana_suma(lista))


if __name__ == "__main__":
    main()