def potegowanie(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    if wykladnik == 1:
        return podstawa

    polowa_wykladnika = wykladnik // 2
    polowa = potegowanie(podstawa, polowa_wykladnika)
    calosc = polowa * polowa

    if wykladnik % 2 == 0:
        return calosc
    else:
        return calosc * podstawa


def main():
    print(potegowanie(2, 78))


if __name__ == "__main__":
    main()