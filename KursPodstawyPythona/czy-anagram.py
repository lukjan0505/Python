def czy_anagram1(napis1, napis2):
    return sorted(napis1) == sorted(napis2)

def czy_anagram2(napis1, napis2):
    lista1 = list(napis1)
    lista2 = list(napis2)
    lista1.sort()
    lista2.sort()
    return lista1 == lista2

def czy_anagram3(napis1, napis2):
    n = len(napis1)
    if n != len(napis2):
        return False
    slownik1 = dict()
    slownik2 = dict()

    for i in range(0, n):
        if napis1[i] in slownik1:
          slownik1[napis1[i]] += 1
        else:
            slownik1[napis1[i]] = 1

        if napis2[i] in slownik2:
          slownik2[napis2[i]] += 1
        else:
            slownik2[napis2[i]] = 1

    # print(slownik1)
    # print(slownik2)
    return slownik1 == slownik2
def main():
    napis1 = "!abCanCa@"
    napis2 = "Cab!anC@a"

    # print(list(napis1).sort())
    # print(list(napis2).sort())
    print(czy_anagram1(napis1, napis2))
    print()
    print(czy_anagram2(napis1, napis2))
    print()
    print(czy_anagram3(napis1, napis2))



if __name__ == "__main__":
    main()