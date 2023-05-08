def dzielenie(dzielna, dzielnik):
    return (dzielna//dzielnik, dzielna % dzielnik)

def main():
    krotka = 2, "Napis", 3.8j
    wynik = dzielenie(7,3)
    print(wynik)
    print(krotka)

    iloraz, reszta = dzielenie(7, 3)
    print(f"iloraz: {iloraz}")
    print(f"reszta: {reszta}")

if __name__ == "__main__":
    main()