"""
Dane jest N kaczuszek gumowych, które należy ułożyć w rzędzie.
Każda kaczuszka ma określoną wysokość i szerokość.
Potrzebujemy ułożyć kaczuszki w taki sposób, aby suma wysokości wykorzystanych kaczuszek była jak największa,
a ich sumaryczna szerokość nie przekroczyła maksymalnej szerokości rzędu.

Wejście: W pierwszym wierszu standardowego wejścia znajdują się
dwie liczby całkowite N, M (1 <= N, M <= 50) pooddzielane
pojedynczymi odstępami oznaczające odpowiednio: liczbę dostępnych kaczuszek oraz maksymalną szerokość rzędu.
W każdym kolejnym N wierszu znajdują się dwie liczby całkowite w, s (1 <= w, s <=9)
oddzielone pojedynczym odstępem oznaczające wysokość (w) i szerokość (s) kaczuszki
Wyjście: Twój program powinien wypisać na standardowe wyjście maksymalną dostępną
sumę wysokości użytych kaczuszek do ustawienia ich w rzędzie.
"""


def main():
    # Zmienne
    indexes = []
    roznica = []
    s_max = 0
    w_max = 0
    wysokosci_kaczek = [3, 5, 7, 2, 8, 4, 6, 9, 1, 5, 7, 8, 3, 4, 6, 2, 1, 5, 8, 9]  # Wysokość kaczek
    szerokosci_kaczek = [2, 4, 6, 1, 5, 3, 7, 9, 2, 4, 6, 8, 3, 5, 7, 1, 2, 4, 6, 8]  # Szerokość kaczek

    n, m = eval(input("Wpisz liczbę kaczek n i szerokość rzędu m po przecinku: "))

    # Obliczanie różnicy wysokości i szerokości kaczki
    for index in range(0, n):
        r = wysokosci_kaczek[index] - szerokosci_kaczek[index]
        roznica.append(r)
        index += 1

    # Wyznaczanie kolejności układania kaczek, sumowanie wysokości, sumowanie szerokości
    #for index in enumerate(roznica):
    while s_max < m:
        i = int(roznica.index(max(roznica)))
        indexes.append(i)
        w_max = wysokosci_kaczek[i] + w_max
        s_max = szerokosci_kaczek[i] + s_max
        roznica[i] = 0

    print("Maksymalna wysokość: ", w_max)

if __name__ == "__main__":
    main()


