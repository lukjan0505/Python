import random


def load_word_from_dictionary():
    file = open("dictionary2.txt")
    random_word = random.choice(file.readlines())
    file.close()
    return random_word.strip()


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def show_state_of_game():
    print()
    print(" ".join(user_word))
    print("Pozostałe próby: ", no_of_tries)
    print("Uzyte litery: ", used_letters, "\n")


def check_letter():
    letter = input("Podaj literę: ")
    if not(letter.isalpha()) or len(letter) > 1:
        print("Podałeś nie właściwą wartość")
    else:
        return letter

# zmienne
used_letters = []
user_word = []
word = load_word_from_dictionary()
no_of_tries = len(word)
number_of_wins = 0
number_of_loss = 0

for _ in word:
    user_word.append("_")

print("Odgadnij jakie to słowo", " ".join(user_word))

while True:
    letter = check_letter()
    if letter not in used_letters:
        used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        no_of_tries -= 1

        if no_of_tries == 0:
            number_of_loss += 1
            print("Koniec rundy!")
            print("Liczba wygranych: ", number_of_wins)
            print("Liczba przegranych: ", number_of_loss)

    else:
        for index in found_indexes:
            user_word[index] = letter
            print("Odgadłeś literę: ", letter)

    if "".join(user_word) == word:
        number_of_wins += 1
        print("Brawo! Odgadłeś słowo: ", word)
        print("Liczba wygranych: ", number_of_wins)
        print("Liczba przegranych: ", number_of_loss)
        continue
    show_state_of_game()
