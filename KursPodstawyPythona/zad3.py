"""
Zadanie 3.** Dla liczb z zakresu od 1 do `N` wypisz liczby, które są podzielne przez 15, 5 i 3 w następujący sposób:

gdy liczba jest podzielna przez 15, wypisz "Liczba `X` jest podzielna przez 15", gdzie `X` to rozpatrywana liczba.

Gdy liczba jest podzielna przez 5, wypisz "Liczba `X` jest podzielna przez 5". Gdy liczba jest podzielna przez 3,

wypisz "Liczba `X` jest podzielna przez 3".

Dla każdej liczby należy wypisać maksymalnie jeden napis. Przetestuj kod dla `N` = 20
"""

def main():
    n = 20
    for x in range(1, n+1):
        if x % 3 == 0:
            print(f"Liczba {x} jest podzielna przez 3.")
        if x % 5 == 0:
            print(f"Liczba {x} jest podzielna przez 5.")
        if x % 15 == 0:
            print(f"Liczba {x} jest podzielna przez 15.")


if __name__ == "__main__":
    main()