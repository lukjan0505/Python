"""
Zadanie 10.** Zmodyfikuj funkcję z poprzedniego zadania, tak aby, w przypadku,

gdy liczba wystąpi więcej niż raz w danej liście / tablicy / wektorze,

zwróć pozycję jej ostatniego wystąpienia.
"""
def szukaj(l, x):
    global ostatni
    for index, wartosc in enumerate(l):
        if l[index] == x:
            ostatni = -1
            if index > ostatni:
                ostatni = index
    return print(ostatni)



def main():
    l = [4, 99, 14, 45, 99, 89, 63, 99, 74, 99, 55]
    x = 99
    szukaj(l, x)



if __name__ == "__main__":
    main()