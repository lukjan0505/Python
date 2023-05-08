import math
class Wspolrzedne:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc_pomiedzy_punktami(self, inny):  # zwykła metoda
        return math.sqrt((self.x - inny.x) ** 2 + (self.y - inny.y) ** 2)

    @staticmethod
    def odleglosc_pomiedzy_punktami_stat(punktA, punktB):  # statyczna metoda
        return math.sqrt((punktA.x - punktB.x) ** 2 + (punktA.y - punktB.y) ** 2)


def main():
    A = Wspolrzedne(3, 4)
    B = Wspolrzedne(-3, -4)

    od1 = A.odleglosc_pomiedzy_punktami(B)
    od2 = A.odleglosc_pomiedzy_punktami_stat(A, B)
    print(f"Odległość punktu ({A.x},{A.y}) od ({B.x},{B.y}) wynosi {od1} ")
    print(f"Odległość punktu ({A.x},{A.y}) od ({B.x},{B.y}) wynosi {od2} ")

if __name__ == "__main__":
    main()