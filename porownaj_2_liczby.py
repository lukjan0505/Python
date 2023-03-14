name=input("Cześć, jak masz na imię? ")
print("Cześć "+name+", chciał bym dla ciebie porównać dwie liczby.")
print("Napisz tak jezli się zgadzasz lub nie jeżli chcesz przerwać.")
odpowiedz=input("Podaj odpowiedź:")
if odpowiedz=="tak":
    print("Świetnie, ze się zgadzasz, podaj pierwszą liczbę:")
    a=input()
    print("Podaj drugą liczbę:")
    b=input()
    if a>b:
        print("Liczba pierwsza "+a+" jest większa od liczby "+b)
    elif b>a:
        print("Liczba druga "+b+" jest większa od liczby "+a)
    else:
        print("Liczby są równe.")
elif odpowiedz=="nie":
    print("Szkoda, ze się nie zgadzasz, do widzenia!")
else:
    print("Zła odpowiedz!")
