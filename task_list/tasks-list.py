import os
user_choice = 0
tasks = []

# pokaz zadania
def show_tasks():
    task_index = 0
    if len(tasks) == 0:
        print("Lista zadań jest pusta! Wczytaj zadania z pliku.")
    else:
        for task in tasks:
            print(task + " [" + str(task_index)+"]")
            task_index += 1

# dodaj zadanie
def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")
    
# usuń zadanie
def delate_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje.")
        return

    tasks.pop(task_index)
    print("Usunięto zadanie!")
    
# zapisz zadania do pliku txt
def save_tasks_to_file():
    print("Domyślna nazwa pliku \"tasks\"")
    nazwa_pliku = input("Podaj nazwę pliku: ")+(".txt")
    file = open(nazwa_pliku, "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()
    print("Zapisano do pliku ", os.getcwd(), "/", nazwa_pliku)

# zapisz zadania do pliku tasks.txt przy wyjściu
def save_tasks_to_file_on_quit():
    quit_program = input(
        "Czy zapisać zmiany do pliku \"tasks.txt\"?\n y - tak lub naciśnij dowolny klawisz aby wyjść... \n")
    if quit_program == "y":
        # nazwa_pliku = input("tasks.txt")
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task+"\n")
        file.close()
        print("Zapisano do pliku ", os.getcwd(), "/", "tasks.txt")

# ładowanie zadań z pliku txt
def load_tasks_from_file():
    try:
        print("Domyślna nazwa pliku \"tasks\"")
        nazwa_pliku = input("Podaj nazwę pliku: ")+(".txt")
        file = open(nazwa_pliku)

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        print("Nie odnaleziono pliku.")
    else:
        print("Plik został wczytany", os.getcwd(), "/", nazwa_pliku)
        return
    
while True:
    if user_choice == 1:
        load_tasks_from_file()

    if user_choice == 2:
        show_tasks()

    if user_choice == 3:
        add_task()

    if user_choice == 4:
        delate_task()

    if user_choice == 5:
        save_tasks_to_file()

    if user_choice == 0:
        print(
            "Witam w programie - Lista zadań. Z dostępnych opcji wybierz co chcesz zrobić.")

    print()
    print("1. Wczytaj zadania z pliku")
    print("2. Pokaz zadania")
    print("3. Dodaj zadanie")
    print("4. Usuń zadanie")
    print("5. Zapisz zmiany do pliku")
    print("6. Wyjdź")
    print("0. Opis")
    try:
        user_choice = int(input("Wybierz liczbę: "))
        print()
    except ValueError:
        print("Nie dokonano właściwego wyboru! Podaj liczbę.")
    else:
        if user_choice < 0 or user_choice > 6:
            print("Nie dokonano właściwego wyboru! Liczba z poza zakresu.")
    if user_choice == 6:
        save_tasks_to_file_on_quit()
        break
    else:
        continue
