class Licznik:
    ile = 0 # pole statyczne
    def __init__(self):
        Licznik.ile += 1
        self.ktory = Licznik.ile
        print(f"To jest obiekt nr {self.ktory}")


    def __del__(self): # destyruktor - używamy do niszczenia
        Licznik.ile -= 1
        print(f"Niszczę obiekt nr {self.ktory}, pozostało jeszcze {Licznik.ile}")


    @staticmethod
    def policz():
        return Licznik.ile # w statycznych metodach odwołujemy się tylko do statycznych pól (zmiennych klasy)

def main():
    a = Licznik()
    b = Licznik()
    c = Licznik()
    print(f"a to obiekt {a.ktory}")
    print(f"b to obiekt {b.ktory}")
    print(f"c to obiekt {c.ktory}")
    print(f"Liczba obiektów to {Licznik.policz()}") # wywołanie metody statycznej
    # print(f"Liczba obiektów to {Licznik.ile}") # wywołanie pola
    a = None  # wywołanie destruktora, obiekt jest niszczony
    b = None  # wywołanie destruktora, obiekt jest niszczony
    print(f"Liczba obiektów to {Licznik.policz()}")  # wywołanie metody statycznej



if __name__ == "__main__":
    main()