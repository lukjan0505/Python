import math


class Wspolrzedne:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        delta = float(self.b ** 2 - 4 * self.a * self.c)
        if delta > 0:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return print(f"Delta wynosi {delta}, pierwiastki to: x1={x1}, x2={x2}")
        if delta == 0:
            x0 = -self.b / (2 * self.a)
            return print(f"Delta wynosi {delta}, pierwiastek podwójny to: x0={x0}")
        return print(f"Brak pierwiastków, delta<0 i wynosi {delta}")


def main():
    # (-1, 3, 4)
    while True:
        try:
            a = int(input("Podaj zmienną a: "))
            if a != 0:
                b = int(input("Podaj zmienną b: "))
                c = int(input("Podaj zmienną c: "))
                wspolczynniki = Wspolrzedne(a, b, c)
                print(f"Rozwiązanie równania kwadratowego {wspolczynniki.a}x^2+{wspolczynniki.b}x+{wspolczynniki.c} ")
                wspolczynniki.rozwiaz()
                break
            else:
                print("Współczynnik a=0 - brak pierwiastków.")
                break
        except ValueError:
            print("Nie podałeś liczby.")
            continue


if __name__ == "__main__":
    main()