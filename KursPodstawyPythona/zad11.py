"""
Zadanie 11.** Napisz funkcję, która dla danej listy / tablicy / wektora,

zwraca listę zawierająca tylko liczby dodatnie.
"""


def szukaj(lista):
    lista_dodatnia = []
    for wartosc in lista:
        if wartosc > 0:
            lista_dodatnia.append(wartosc)
    return lista_dodatnia


def main():
    lista = [4, -63, 14, 45, -9, 89, 63, -99, 74, 69, -55]
    print(szukaj(lista))


if __name__ == "__main__":
    main()