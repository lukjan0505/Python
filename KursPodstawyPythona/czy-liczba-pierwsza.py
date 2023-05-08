import math
liczba = 0
def czy_liczba_pierwsza(liczba):
    czy_pierwsza = "Liczba pierwsza"
    if liczba % 2 == 0 and liczba > 2:
        czy_pierwsza = "to nie liczba pierwsza"
    else:
        for i in range(2, int(math.sqrt(liczba))):
            if liczba % i == 0:
                czy_pierwsza = "to nie liczba pierwsza"
                break
    return czy_pierwsza




def main():
    liczba =int(input("Podaj liczbę: "))
    print(czy_liczba_pierwsza(liczba))


if __name__ == "__main__":
    main()