lista = [2, -8, 4, 6]

def srednia(liczby):
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma / len(liczby)
def check(lista):
    wynik = 0
    for liczba in lista:
        if liczba < 0:
            wynik = "Nie wszystkie elementy są dodatnie"
            break
        else:
            wynik = "Wszystkie elementy są dodatnie"
    return wynik

def main():
    print(check(lista))


if __name__ == "__main__":
    main()