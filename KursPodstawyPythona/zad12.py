"""
Zadanie 12.** Zmodyfikuj funkcję z poprzedniego zadania tak,

aby funkcja przyjmowała dwa argumenty:

listę / tablicę / wektor oraz napis: `"dodatnie"` lub `"ujemne"`.

Funkcja ma zwracać listę / tablicę / wektor zawierającą elementy dodatnie lub

ujemne w zależności od tego, jaki napis został podany.

W przypadku, gdy napis nie jest żadnym z dwóch dostępnych napisów (`"dodatnie"` lub `"ujemne"`),

zwróć pustą listę / tablicę / wektor.
"""
user_choice = 0
napis = ""
def szukaj(lista, napis):
    lista_sortowana = []
    for wartosc in lista:
        if napis == "dodatnie" and wartosc > 0:
            lista_sortowana.append(wartosc)
        if napis == "ujemne" and wartosc < 0:
            lista_sortowana.append(wartosc)
    return lista_sortowana


def main():
    lista = [4, -63, 14, 45, -9, 89, 63, -99, 74, 69, -55]
    print("Jakie liczby wyświetlić? ")
    print("1. dodatnie")
    print("2. ujemne")
    user_choice = input("Wybierz 1 lub 2: ")
    if user_choice == "1":
        napis = "dodatnie"
        print(szukaj(lista, napis))
    elif user_choice == "2":
        napis = "ujemne"
        print(szukaj(lista, napis))
    else:
        lista = []
        print(lista)

if __name__ == "__main__":
    main()