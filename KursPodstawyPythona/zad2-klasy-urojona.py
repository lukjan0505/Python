import math
class LiczbaZespolona:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def wypisz(self):
        if self.b > 0:
            return  str(self.a) + "+" + str(self.b) + str("i")
        if self.b < 0:
            return str(self.a) + str(self.b) + str("i")

    def modul(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    @staticmethod
    def dodaj(liczba1, liczba2):
        a = liczba1.a + liczba2.a
        b = liczba1.b + liczba2.b
        dodawanie = LiczbaZespolona(a, b)
        return dodawanie

    @staticmethod
    def odejmij(liczba1, liczba2):
        a = liczba1.a - liczba2.a
        b = liczba1.b - liczba2.b
        odejmowanie = LiczbaZespolona(a, b)
        return odejmowanie

    @staticmethod
    def mnoz(liczba1, liczba2):
        a = liczba1.a * liczba2.a + liczba1.b * liczba2.b * (-1)
        b = liczba1.a * liczba2.b + liczba1.b * liczba2.a
        mnozenie = LiczbaZespolona(a, b)
        return mnozenie

def main():
    liczba1 = LiczbaZespolona(-2, 5)
    liczba2 = LiczbaZespolona(-2, 5)
    liczba1.wypisz()
    liczba2.wypisz()
    suma = LiczbaZespolona.dodaj(liczba1, liczba2)
    roznica = LiczbaZespolona.odejmij(liczba1, liczba2)
    iloczyn = LiczbaZespolona.mnoz(liczba1, liczba2)
    print()
    print(f"Moduł z liczby {liczba1.wypisz()} wynosi {liczba1.modul()}")
    print(f"Moduł z liczby {liczba2.wypisz()} wynosi {liczba2.modul()}")
    print()
    print(f"Suma liczb {liczba1.wypisz()} i {liczba2.wypisz()} wynosi {suma.wypisz()}")
    print(f"Różnica liczb {liczba1.wypisz()} i {liczba2.wypisz()} wynosi {roznica.wypisz()}")
    print(f"Iloczyn liczb {liczba1.wypisz()} i {liczba2.wypisz()} wynosi {iloczyn.wypisz()}")
    # suma.wypisz()

if __name__ == "__main__":
    main()