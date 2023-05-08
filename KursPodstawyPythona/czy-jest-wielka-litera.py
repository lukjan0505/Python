def czy_wielka_litera(napis):
    for i in range(len(napis)):
        if napis[i].isupper():
            return "jest wielka litera"
    return "brak wielkiej litery"

def main():
    napis = input("Podaj napis: ")
    print(czy_wielka_litera(napis))



if __name__ == "__main__":
    main()