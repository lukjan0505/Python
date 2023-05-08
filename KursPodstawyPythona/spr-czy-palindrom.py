
def czy_palindrom(napis):
    sprawdzanie = True
    sprawdzany_napis = []
    for litera in napis:
        sprawdzany_napis.append(litera)

    index_count = len(napis)

    i = 1
    for x in range(0, int(index_count // 2)):
        if sprawdzany_napis[x] == sprawdzany_napis[-i]:
            i += 1
        else:
            sprawdzanie = False
    return napis, sprawdzanie

def czy_palindrom2(napis):
    return napis == napis[::-1]

def main():
    napis = "kobyłamamałybok"

    print(czy_palindrom(napis))
    print(len(napis))
    print(czy_palindrom2(napis))


if __name__ == "__main__":
    main()