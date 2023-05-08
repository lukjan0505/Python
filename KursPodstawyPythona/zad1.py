"""
Zadanie 1.** Dla danego dochodu policz podatek na następujących zasadach:
- gdy dochód wynosi mniej niż 85 000, to podatek wynosi 10% z dochodu;
- jeśli dochód jest większy lub równy 85 000, ale mniejszy niż 170 000, to podatek wynosi 15% z dochodu;
- gdy dochód jest większy lub równy 170 000, to podatek wynosi 15% ze 170 000 i 20% z dochodu pomniejszonego o 170 000.

Policz podatek dla następujących dochodów: 36 000, 120 000, 240 000.
"""
def oblicz_podatek(dochod):
    podatek = 0
    if dochod < 85000:
        podatek = 0.1 * dochod
    elif dochod >= 85000 and dochod < 170000:
        podatek = 0.15 * dochod
    elif dochod >= 170000:
        podatek = (0.15 * 170000) + (0.2 * (dochod - 170000))
    else:
        print("Podałeś niepoprawną wartość!")
    return podatek
def main():
    dochod1 = 75000
    dochod2 = 120000
    dochod3 = 1200000


    print(f"Podatek roczny z kwoty {dochod1} zł wynosi {oblicz_podatek(dochod1)} zł")
    print(f"Podatek roczny z kwoty {dochod2} zł wynosi {oblicz_podatek(dochod2)} zł")
    print(f"Podatek roczny z kwoty {dochod3} zł wynosi {oblicz_podatek(dochod3)} zł")


if __name__ == "__main__":
    main()