"""Działania na podanych wielu ułamkach"""
import math
liczniki = []
mianowniki = []
liczby = []

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        # self.skroc()

    def wypisz(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def podaj(self):
        return str(self.licznik), str(self.mianownik)

    def skroc(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd
        if self.mianownik < 0:
            self.licznik *= -1
            self.mianownik *= -1

    # @staticmethod
    # def dodaj(liczniki, mianowniki):
    #     poprzedni = 1
    #     for index, element in enumerate(mianowniki):
    #         mianownik = poprzedni * element
    #         poprzedni = mianownik
    #         return mianownik
    #
    #     # lewy_licznik = u1.licznik * u2.mianownik
    #     # prawy_licznik = u2.licznik * u1.mianownik
    #     # mianownik = u1.mianownik * u2.mianownik
    #     # dodawanie = Ulamek(lewy_licznik + prawy_licznik, mianownik)
    #     # dodawanie.skroc()
    #     return dodawanie

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
    liczba_ulamkow = int(input("Podaj liczbę ułamków: "))
    print("Podaj kolejne ułamki i zatwierdź \"ENTEREM\"")
    # u1 = Ulamek(2,3)
    # u2 = Ulamek(3,4)
    # u3 = Ulamek(2,5)

    for index in range(1, liczba_ulamkow+1):
        licznik, mianownik = eval(input(f"Podaj  licznik i mianownik po przecinku dla ułamka {index}: "))
        liczniki.append(licznik)
        mianowniki.append(mianownik)
        index += 1
    #     # u = Ulamek(licznik, mianownik).podaj()
    #     # liczby.append("2,3")
    #     liczby.append(u[index])
    #     liczby.append("(9,9)")
    #
    #     index += 1



    print(liczniki)
    print(mianowniki)

    # suma = Ulamek.dodaj(u1, u2).wypisz()
    # roznica = Ulamek.odejmij(u1, u2).wypisz()
    # mnozenie = Ulamek.mnoz(u1, u2).wypisz()
    # dzielenie = Ulamek.dziel(u1, u2).wypisz()
    # print(f"Suma ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {suma}")
    # print(f"Różnica ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {roznica}")
    # print(f"Mnożenie ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {mnozenie}")
    # print(f"Dzielenie ułamków {u1.wypisz()} i {u2.wypisz()} wynosi {dzielenie}")


if __name__ == "__main__":
    main()
