"""Module providingFunction printing python version."""
import math # [Importowanie funkcji matematycznej]
print("Program rozwiązuje pierwiastki równania kwadratowego zupełnego w postaci ax^2+bx+c=0.")
while True:
    try:
        a = int(input("Podaj zmienną a: "))
        if a != 0:
            b = int(input("Podaj zmienną b: "))
            c = int(input("Podaj zmienną c: "))
            delta = float(b ** 2-4*a*c)
            if delta > 0:
                x1 = (-b+math.sqrt(delta))/(2*a)
                x2 = (-b-math.sqrt(delta))/(2*a)
                print("Delta wynosi: "+str(delta))
                print("Pierwiastek x1="+str(x1))
                print("Pierwiastek x2="+str(x2))
            elif delta == 0:
                x0 = -b/(2*a)
                print("Pierwiastek x0="+str(x0))
            else:
                print("Brak pierwiastków, delta<0 i wynosi "+str(delta))
        else:
            print("Brak pierwiastków.")
            print("Współczynnik a=0.")
    except ValueError:
        print("Nie podałeś liczby.")
        continue
    else:
        break
    