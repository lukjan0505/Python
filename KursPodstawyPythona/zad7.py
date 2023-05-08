"""
Zadanie 7.** Napisz funkcję, która dla danej listy / tablicy / wektora zwraca listę / tablicę / wektor,

składającą się tylko z elementów leżących na parzystych pozycjach.
"""
def lista_z_parzystymi_pozycjami(lista):
    parzyste = []
    for index, wartosc in enumerate(lista):
        if index % 2 == 0:
            parzyste.append(wartosc)
    return parzyste
def main():
    lista = [4, 63, 14, 45, 9, 89, 63, 99, 74, 69, 55]
    print(lista_z_parzystymi_pozycjami(lista))

if __name__ == "__main__":
    main()