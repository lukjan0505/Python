class Test:
    def __init__(self):
        self.publiczne = 3
        self._chronione = 2
        self.__prywatne = 1

    def __tajna(self):
        print("Tajna informacja")

def main():
    test = Test()
    print(test.publiczne)
    test.publiczne = 7
    print(test.publiczne)

    print(test._chronione)
    test._chronione = 8
    print(test._chronione)

    print(test._Test__prywatne)
    test._Test__prywatne = 9
    print(test._Test__prywatne)

    test._Test__tajna()

if __name__ == "__main__":
    main()