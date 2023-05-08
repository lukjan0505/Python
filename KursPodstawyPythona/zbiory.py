def main():
    zbior_pusty = set()
    print(zbior_pusty)
    zbior = {1, 2, 3, 5}
    zbior2 = {8, 6, 5, 3, 1, 2}
    # zbior.add(8)
    print(zbior)
    print(5 in zbior)
    print()

    print(zbior | zbior2)  # suma zbiorów
    print(zbior - zbior2)  # suma różnica
    print(zbior & zbior2)  # suma przecięcie- część wspólna
    print(zbior.issubset(zbior2))  # czy zbior jest podzbiorem zbioru2


if __name__ == "__main__":
    main()