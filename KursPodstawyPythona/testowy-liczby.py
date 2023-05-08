
liczby = []
mianowniki = [2, 3, 4]
# for index in range(0,3):
#     l = int(input("Podaj liczbę: "))
#     liczby.append(l)

mianownik = 1
poprzedni = 1
for index, element in enumerate(mianowniki):
    mianownik = poprzedni * element
    poprzedni = mianownik




print(liczby)
print(mianownik)