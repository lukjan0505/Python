import math
class Wspolrzedne:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc_od_srodka_ukladu(self):
        odleglosc = math.sqrt(self.x ** 2 + self.y ** 2)
        return odleglosc


def main():
    p = Wspolrzedne(2, 4)
    print(f"Odległość punktu ({p.x},{p.y}) od środka układ współrzędnych wynosi {p.odleglosc_od_srodka_ukladu()} ")


if __name__ == "__main__":
    main()