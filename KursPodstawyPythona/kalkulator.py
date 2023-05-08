def main():
    user_choice = "t"
    wynik = 0
    while user_choice != "n":
        print("Kalkulator")
        a = float(input("Podaj pierwszą liczbę: "))
        dzialanie = input("Podaj działanie: ")
        b = float(input("Podaj drugą liczbę: "))

        if dzialanie == "+":
            wynik = a + b
        elif dzialanie == "-":
            wynik = a - b
        elif dzialanie == "*":
            wynik = a * b
        elif dzialanie == "/":
            wynik = a / b
        elif dzialanie == "//":
            wynik = a // b
        elif dzialanie == "%":
            wynik = a % b
        else:
            print("Nie podałeś prawidłowego działania!")

        print(f"Wynik działania: {wynik}")
        user_choice = input("Czy chcesz wykonać kolejne działanie? Wpisz t lub n: ")


if __name__ == "__main__":
    main()
