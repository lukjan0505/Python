"""Działania na ułamkach dla podanych dwóch ułamków"""
import math


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = int(licznik)
        self.mianownik = int(mianownik)
        # self.skroc()

    def wypisz(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def skroc(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd
        if self.mianownik < 0:
            self.licznik *= -1
            self.mianownik *= -1

    @staticmethod
    def dodaj(u1, u2):
        lewy_licznik = u1.licznik * u2.mianownik
        prawy_licznik = u2.licznik * u1.mianownik
        mianownik = u1.mianownik * u2.mianownik
        dodawanie = Ulamek(lewy_licznik + prawy_licznik, mianownik)
        dodawanie.skroc()
        return dodawanie

    @staticmethod
    def odejmij(u1, u2):
        lewy_licznik = u1.licznik * u2.mianownik
        prawy_licznik = u2.licznik * u1.mianownik
        mianownik = u1.mianownik * u2.mianownik
        odejmowanie = Ulamek(lewy_licznik - prawy_licznik, mianownik)
        odejmowanie.skroc()
        return odejmowanie

    @staticmethod
    def mnoz(u1, u2):
        mianownik = u1.mianownik * u2.mianownik
        licznik = u1.licznik * u2.licznik
        mnozenie = Ulamek(licznik, mianownik)
        mnozenie.skroc()
        return mnozenie

    @staticmethod
    def dziel(u1, u2):
        mianownik = u1.mianownik * u2.licznik
        licznik = u1.licznik * u2.mianownik
        dzielenie = Ulamek(licznik, mianownik)
        dzielenie.skroc()
        return dzielenie


def main():
    u1_licznik, u1_mianownik = eval(input(f"Podaj po przecinku licznik i mianownik dla ułamka pierwszego: "))
    u1 = Ulamek(u1_licznik, u1_mianownik)
    u2_licznik, u2_mianownik = eval(input(f"Podaj po przecinku licznik i mianownik dla ułamka drugiego: "))
    u2 = Ulamek(u2_licznik, u2_mianownik)
    suma = Ulamek.dodaj(u1, u2).wypisz()
    roznica = Ulamek.odejmij(u1, u2).wypisz()
    mnozenie = Ulamek.mnoz(u1, u2).wypisz()
    dzielenie = Ulamek.dziel(u1, u2).wypisz()
    print(f"Suma ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {suma}")
    print(f"Różnica ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {roznica}")
    print(f"Mnożenie ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {mnozenie}")
    print(f"Dzielenie ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {dzielenie}")


if __name__ == "__main__":
    main()
