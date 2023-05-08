class Taksi:
    def __init__(self, koszt_wejscia, koszt_kilometra):
        self.koszt_wejscia = koszt_wejscia
        self.koszt_kilometra = koszt_kilometra


    def koszt_przejazdu(self, km):
        koszt = self.koszt_wejscia + km * self.koszt_kilometra
        return koszt


def main():
    stawka_HalloTaxi = Taksi(5, 6)
    stawka_BobTaxi = Taksi(4, 5)
    dystans = int(input("Jaki dystans chcesz przejechać? "))
    print(f"Koszt przejazdu {dystans}km w Hallo Taxi to {stawka_HalloTaxi.koszt_przejazdu(dystans)}")
    print(f"Koszt przejazdu {dystans}km w Bob Taxi to {stawka_BobTaxi.koszt_przejazdu(dystans)}")


if __name__ == "__main__":
    main()
