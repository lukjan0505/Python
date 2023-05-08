"""
Zadanie 13.** Zmodyfikuj funkcję z poprzedniego zadania tak,

aby funkcja domyślnie przyjmowała napis `"dodatnie"`.
"""
user_choice = 0
napis = "dodatnie"
def szukaj(lista, napis='dodatnie'):
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
    user_choice = input("Wybierz dodatnie lub ujemne: ")
    if user_choice == "dodatnie":
        napis = "dodatnie"
        print(szukaj(lista, napis))
    elif user_choice == "ujemne":
        napis = "ujemne"
        print(szukaj(lista, napis))
    elif user_choice == "":
        napis = "dodatnie"
        print(szukaj(lista, napis))
    else:
        lista = []
        print(lista)



if __name__ == "__main__":
    main()