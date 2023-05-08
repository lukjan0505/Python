def main():
    baza_danych_polakow = {"89082911250" : ["Jan", "Kowalski", 29],
                           "78524654125" : ["Ania", "Nowak", 23],
                           "13465789154" : ["Adam", "Mickiewicz", 220]
                           }
    print(baza_danych_polakow)
    print("89082911250" in baza_danych_polakow)
    print("89082911250" not in baza_danych_polakow)
    print(baza_danych_polakow.get("13465789000", "Brak wartości" )) # sprawdzanie czy jest wartosc
    baza_danych_polakow["54187987788"] = ["Magda", "Domel", 28]
    del baza_danych_polakow["13465789154"]
    print(baza_danych_polakow)

    for klucz in baza_danych_polakow.keys():
        print(klucz)

    for wartosc in baza_danych_polakow.values():
        print(wartosc)

    for klucz, wartosc in baza_danych_polakow.items():
        print(klucz, wartosc)

if __name__ == "__main__":
    main()