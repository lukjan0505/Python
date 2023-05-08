
def silnia(n):
    if n < 0:
        raise ValueError("Silnia niezdefiniowana dla liczb ujemnych") # rzucanie wyjątków
    wynik = 1
    for i in range(1, n+1):
        wynik *= 1
    return  wynik

def main():
    napis_wczytany = "-2"
    try:
        print("pozyskuje zasób")
        liczba = float(napis_wczytany)
        print(silnia(liczba))

        # print(liczba/0)
    except ValueError as e:
        print("Nie udało się sparsować liczby! Szczegóły poniżej: ")
        print(e)
    except ZeroDivisionError as e:
        print("Nie dziel przez zero.")
    finally:
        print("zwalnia zasób") # zwalnia zasób

    print("Reszta programu")


if __name__ == "__main__":
    main()