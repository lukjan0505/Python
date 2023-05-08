"""
Zadanie 6.** Napisz funkcję `czy_wielka`, przyjmującą na wejściu napis.

Jako wynik zwróć wartość logiczną (`True` / `False`), informującą, czy podany napis zaczyna się wielką literą.
"""
def czy_wielka(napis):
    for i in range(len(napis)):
        if napis[i].isupper():
            return True
    return False
def main():
    napis = "Wielka"
    print(czy_wielka(napis))



if __name__ == "__main__":
    main()