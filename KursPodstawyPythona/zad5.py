"""
Zadanie 5.** Napisz funkcję, która dla podanych trzech argumentów, zwraca ich maksimum, nie używając funkcji `max()`.

Przetestuj kod dla danych trójek: `1, 2, 3`; `4, 6, 5`; `9, 8, 7`.
"""
def maksymalna_wartosc(a, b, c):
    max_wartosc = 0
    if a > b and a > c:
        max_wartosc = a
    elif b > c and b > a:
        max_wartosc = b
    elif c > b and c > a:
        max_wartosc = c
    return max_wartosc

def maksymalna_wartosc2(liczby):
    maks = 0
    for ile in liczby:
        if ile > maks:
            maks = ile
    return maks
def main():
    para1 = [1, 2, 3]
    para2 = [4, 6, 5]
    para3 = [9, 8, 7]

    print(maksymalna_wartosc(1, 2, 3))
    print(maksymalna_wartosc(4, 6, 5))
    print(maksymalna_wartosc(9, 8, 7))
    print()
    print(maksymalna_wartosc2(para1))
    print(maksymalna_wartosc2(para2))
    print(maksymalna_wartosc2(para3))

if __name__ == "__main__":
    main()