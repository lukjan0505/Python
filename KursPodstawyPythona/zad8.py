"""
Zadanie 8.** Napisz funkcję, która dla danego `n`

z zakresu od 1 do 9 zwraca wynik następującego dodawania: `n + nn + nnn`.

Przykładowo, dla `n = 5` zwrócimy wynik dodawania `5 + 55 + 555`.
"""
def dodawanie(n):
    wynik = 0
    for x in range(1, n+1):
        wynik = 123 * x
        print(wynik)
    return wynik

def suma(n):
    nn = 10*n + n
    nnn = 100*n + 10*n + n
    return n + nn + nnn


def dodawanie2(n):
    wynik = 0
    for x in range(1, n+1):
        print(f"{str(x)}+{str(x)+str(x)}+{str(x)+str(x)+str(x)} = {123 * x}")
    return wynik
def main():
    n = 5
    dodawanie(n)
    print()
    dodawanie2(n)



if __name__ == "__main__":
    main()