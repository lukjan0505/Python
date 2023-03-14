# Gra polega na odgadnięciu słowa przy podanej liczbie prób
import random
import datetime
user_choice = 0
number_off_wins_one = 0
number_off_loss_one = 0
number_off_wins_two = 0
number_off_loss_two = 0
players = []
results_h = []


class Game:
    def __init__(self):
        self.random_word = None
        self.unknown_word = []

    def load_word_from_dictionary(self):
        file = open("dictionary.txt", encoding="utf-8")
        self.random_word = str(random.choice(file.readlines()))
        file.close()
        return self.random_word.strip()

    def word_of_user(self, word_c):
        for _ in word_c:
            self.unknown_word.append("_")
        return self.unknown_word


# Wybór użytkownika w głównym menu gry
def choice():
    try:
        user_choice_a = int(input("Wybierz liczbę: "))
        if user_choice_a > 5 or user_choice_a < 0:
            print("Liczba z poza zakresu! Wybierz liczbę.")
            print()
    except ValueError:
        print("Nie dokonano właściwego wyboru! Wybierz liczbę.")
    else:
        return user_choice_a
    

# Status w trakcie rundy
def state(unknown_word_c, no_of_tries_c, used_letters_c, player_c):
    print()
    print('\x1b[38;2;255;255;255m\x1b[48;2;0;0;255m'+" ".join(unknown_word_c)+'\x1b[0m')
    print("Pozostałe próby: ", '\x1b[38;2;255;255;255m\x1b[48;2;170;0;0m' + str(no_of_tries_c) + '\x1b[0m')
    print("Użyte litery: ", '\x1b[38;2;255;255;255m\x1b[48;2;0;128;128m' + str(used_letters_c) + '\x1b[0m')
    print("Gracz: ", '\x1b[38;2;255;255;255m\x1b[48;2;128;128;0m' + player_c + '\x1b[0m', "\n")


# Wykrywa czy w nieznanym słowie znajduje się litera, jeżeli tak, zastępuje "_" podaną literą
def find_indexes(word_c, letter_c):
    indexes = []
    for index_c, letter_in_word in enumerate(word_c):
        if letter_c == letter_in_word:
            indexes.append(index_c)
    return indexes


def show_results():
    if len(players) == 1:
        p1 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_one,
                                                                str(number_off_wins_one),
                                                                str(number_off_loss_one),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        print('\x1b[38;2;255;255;255m\x1b[48;2;0;128;0m' + p1 + '\x1b[0m')
    else:
        p1 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_one,
                                                                str(number_off_wins_one),
                                                                str(number_off_loss_one),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        p2 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_two,
                                                                str(number_off_wins_two),
                                                                str(number_off_loss_two),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        print('\x1b[38;2;255;255;255m\x1b[48;2;0;128;0m' + p1 + '\x1b[0m')
        print('\x1b[38;2;255;255;255m\x1b[48;2;0;128;0m' + p2 + '\x1b[0m')


def save_results_to_file_on_quit():
    if len(players) == 1:
        p1 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_one,
                                                                str(number_off_wins_one),
                                                                str(number_off_loss_one),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        file = open("results.txt", "a+")
        file.write(p1)
        file.close()
    else:
        p1 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_one,
                                                                str(number_off_wins_one),
                                                                str(number_off_loss_one),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        p2 = "{0} * Wygrane-{1} * Przegrane-{2} * {3}\n".format(player_two,
                                                                str(number_off_wins_two),
                                                                str(number_off_loss_two),
                                                                str(datetime.datetime.now().strftime(
                                                                    '%H:%M  %d-%m-%y')))
        file = open("results.txt", "a+")
        file.write(p1)
        file.write(p2)
        file.close()


def load_results_on_start():
    file = open("results.txt")
    for line in file.readlines():
        results_h.append(line)
    file.close()
    

def change_user(player_c):
    if player_c == player_one:
        player_c = player_two
    else:
        player_c = player_one
    return player_c


###############################################
player_one = input("Wprowadź imię gracza: ")
players.append(player_one)
load_results_on_start()
while True:
    if user_choice == 1:
        runda = Game()
        word = runda.load_word_from_dictionary()
        unknown_word = runda.word_of_user(word)
        no_of_tries = len(word)
        user_word = []
        used_letters = []
        print("Odgadnij jakie to słowo: ", '\x1b[38;2;255;255;255m\x1b[48;2;0;0;255m'+" ".join(unknown_word)+'\x1b[0m')
        while True:
            letter = input("Podaj literę: ")
            if not (letter.isalpha()) or len(letter) > 1:
                print("Podałeś nie właściwą wartość")
            else:
                if letter not in used_letters:
                    used_letters.append(letter)
                found_indexes = find_indexes(word, letter)
                if len(found_indexes) == 0:
                    print("Nie ma takiej litery")
                    no_of_tries -= 1
                    if no_of_tries == 0:
                        print("Przegrałeś!")
                        print("Zgadywane słowo: ", '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + word + '\x1b[0m')
                        number_off_loss_one += 1
                        show_results()
                        break
                else:
                    for index in found_indexes:
                        unknown_word[index] = letter
                if "".join(unknown_word) == word:
                    print("Wygrałeś! Odgadłeś słowo: ", '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + word + '\x1b[0m')
                    number_off_wins_one += 1
                    show_results()
                    break
            state(unknown_word, no_of_tries, used_letters, player_one)
            continue

    if user_choice == 2:
        runda = Game()
        word = runda.load_word_from_dictionary()
        unknown_word = runda.word_of_user(word)
        no_of_tries = len(word)
        user_word = []
        used_letters = []
        if len(players) == 1:
            player_two = input("Wprowadź imię  drugiego gracza: ")
            players.append(player_two)
            continue
        else:
            player = random.choice(players)
            print("Odgadnij jakie to słowo: ",
                  '\u001B[38;2;255;255;255m\u001B[48;2;0;0;255m{0}\u001B[0m'.format(" ".join(unknown_word)))
            print("Gracz: ", '\x1b[38;2;255;255;255m\x1b[48;2;128;128;0m' + player + '\x1b[0m', "\n")
            while True:
                letter = input("Podaj literę: ")
                if not (letter.isalpha()) or len(letter) > 1:
                    print("Podałeś nie właściwą wartość")
                else:
                    if letter not in used_letters:
                        used_letters.append(letter)
                    found_indexes = find_indexes(word, letter)
                    if len(found_indexes) == 0:
                        print("Nie ma takiej litery")
                        no_of_tries -= 1
                        player = change_user(player)
                        if no_of_tries == 0:
                            print("Przegraliście!")
                            print("Zgadywane słowo: ", '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + word + '\x1b[0m')
                            number_off_loss_one += 1
                            number_off_loss_two += 1
                            show_results()
                            break
                    else:
                        for index in found_indexes:
                            unknown_word[index] = letter
                    if "".join(unknown_word) == word:
                        print("Gracz: ", '\x1b[38;2;255;255;255m\x1b[48;2;128;128;0m' + player + '\x1b[0m')
                        print("zgadł słowo:  ", '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + word + '\x1b[0m', "\n")
                        if player == player_one:
                            number_off_wins_one += 1
                        else:
                            number_off_wins_two += 1
                        show_results()
                        break
                state(unknown_word, no_of_tries, used_letters, player)
                continue

    if user_choice == 3:
        show_results()
        
    if user_choice == 4:
        print('\x1b[38;2;255;255;255m\x1b[48;2;0;128;0m' + " ".join(results_h) + '\x1b[0m')
 
    if user_choice == 5:
        save_results_to_file_on_quit()
        print("Wyjście z gry")
        break
        
    if user_choice == 0:
        print("Gra polega na odgadnięciu słowa przy podanej liczbie prób")          
               
    print()
    print("1. Nowa gra - 1 gracz")
    print("2. Nowa gra - 2 graczy")
    print("3. Wyniki aktualnej gry")
    print("4. Wyniki historyczne")
    print("5. Wyjdź z gry")
    print("0. Opis")
    print()
    user_choice = choice()
