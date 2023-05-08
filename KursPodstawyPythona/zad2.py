"""
Zadanie 2.** Dla każdej kwoty z listy / tablicy / wektora `[50000, 10000, 200000, 75000, 1200000]`
oblicz podatek według schematu z poprzedniego zadania i wypisz go w postaci (bez części ułamkowej):

Dochód: 50000, podatek: 5000

Dochód: 10000, podatek: 1000
"""
def oblicz_podatek(dochod):
    podatek = 0
    if dochod < 85000:
        podatek = 0.1 * dochod
    elif dochod >= 85000 and dochod < 170000:
        podatek = 0.15 * dochod
    elif dochod >= 170000:
        podatek = (0.15 * 170000) + (0.2 * (dochod - 170000))
    else:
        print("Podałeś niepoprawną wartość!")
    return int(podatek)
def main():
    lista_dochodow = [50000, 10000, 200000, 75000, 1200000]


    for dochod in lista_dochodow:
        print(f"Dochód: {dochod}, podatek: {oblicz_podatek(dochod)}")



if __name__ == "__main__":
    main()