class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat")

    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed


def main():
    Jan = Osoba("Jan", "Kowalski", 49)
    Adam = Osoba("Adam", "Mickiewicz", 221)
    print(Jan.imie) # Jan
    print(Jan.nazwisko) # Kowalski
    Jan.przedstaw_sie() # Jestem Jan Kowalski. Mam 49 lat
    # Osoba.przedstaw_sie(Jan) # Jestem Jan Kowalski. Mam 49 lat
    Adam.przedstaw_sie() # Jestem Adam Mickiewicz. Mam 221 lat
    print()
    wiek_Adama_przed = Adam.urodziny()
    Adam.przedstaw_sie() # Jestem Adam Mickiewicz. Mam 222 lat
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed} lat") # Wiek Adama sprzed urodzin: 221 lat
    print()
    wiek_Adama_przed = Adam.urodziny() # Jestem Adam Mickiewicz. Mam 223 lat
    Adam.przedstaw_sie()
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed} lat") # Wiek Adama sprzed urodzin: 222 lat

if __name__ == "__main__":
    main()