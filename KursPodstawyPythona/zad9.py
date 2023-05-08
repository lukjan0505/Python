"""
Zadanie 9.** Napisz funkcję `gdzie`, która dla danej listy / tablicy / wektora `l` i liczby `x`,

zwróci pozycję elementu `x` w liście / tablicy / wektorze `l`.

W przypadku, gdy liczba wystąpi więcej niż raz w danej liście / tablicy / wektorze,

zwróć pozycję jej pierwszego wystąpienia.

Jeśli liczba `x` nie występuje w liście / tablicy / wektorze `l`, zwróć `-1`.

Przetestuj kod dla `l = [6, 4, 4, 1, 5, 3, 7, 3]` i `x = 1`, `x = 2`, `x = 3`, `x = 4`.

Celem zadania jest implementacja rozwiązania bez wykorzystania gotowych funkcji rozwiązujących ten problem.
"""


def szukaj(l, x):
    for index, wartosc in enumerate(l):
        if l[index] == x:
            return index
    return -1


def main():
    l = [4, 99, 14, 45, 9, 89, 63, 99, 74, 69, 55]
    x = 3
    print(szukaj(l, x))


if __name__ == "__main__":
    main()