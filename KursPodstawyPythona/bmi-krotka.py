def sprawdzanie_bmi(waga, wzrost):
    wynik = waga / (wzrost ** 2)
    if wynik < 10.5:
        return round(wynik, 0), "niedowaga"
    elif wynik < 25:
        return int(wynik), "optimum"
    else:
        return round(wynik, 0), "nadwaga"
def main():
    waga, wzrost = eval(input("Podaj wagę i wzrost po przecinku:  "))
    print(sprawdzanie_bmi(waga, wzrost))


if __name__ == "__main__":
    main()