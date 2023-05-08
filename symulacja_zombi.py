"""
Symulacja walki ludzi z zombi.

Liczba par -losowa z przedziału (n, m).
Parametry człowieka i zombi:
    (x, y, s) - człowiek/zombi
    x -położenie na osi x
    y -położenie na osi y
    s -siła
    d = sqrt((x2-x1)^2+(y2-y1)^2)

    -w walce biorą udział pary człowiek-zombi, pomiędzy którymi odległość jest mniejsza, równa d,
    -jeżeli nie ma takiej pary, dodawane jest do list po jednym zawodniku, aż warunek odległości będzie spełniony,
    -siła zwycięskiego osobnika po wygranej jest pomniejszana o siłę pokonanego,
    -zwycięzca przechodzi do następnej rundy,
    -przegrany człowiek staje się zombi i zostaje dodany do grupy zombi,
    -jeżeli liczba wygranych u ludzi jest większa niż liczba wygranych u zombi i zawiera się w przedziale
        (t, p), zostaje dodany nowy człowiek,
    -wyliczona odległość jest zmniejszana o 1 w każdej iteracji,
    -jeżeli odległość jest większa niż d, zombi koryguje swoją pozycję w kierunku współrzędnej (0, 0),
    -przegrywa grupa, która zostaje całkowicie wyeliminowana.


"""
from random import choices, randrange
from math import sqrt
min_distance = 4
number_of_players = randrange(50, 51)    # (n, m)
min_coordinate = 1
max_coordinate = 7
humans = [list(choices(range(min_coordinate, max_coordinate), k=3)) for humen in range(number_of_players)]
zombies = [list(choices(range(min_coordinate, max_coordinate), k=3)) for zombi in range(number_of_players)]
print(f"Liczba par: {len(humans)}")


def game_status(zombies_wins, humans_wins, game_in_progress):
    print(f"Zombi: {zombies}")
    print(f"Ludzi: {humans}")
    print(f"Populacja zombi: {len(zombies)} Liczba wygranych: {zombies_wins}")
    print(f"Populacja ludzi: {len(humans)}  Liczba wygranych: {humans_wins}\n")
    if len(zombies) == 0:
        print(f"Ludzie wygrali bitwę, liczba ocalałych: {len(humans)}")
        game_in_progress = False
    elif len(humans) == 0:
        print(f"Zombie wygrały bitwę, liczba ocalałych: {len(zombies)}")
        game_in_progress = False
    elif len(humans) == len(humans) == 0:
        print(f"Remis! Liczba ocalałych: 0")
        game_in_progress = False
    return game_in_progress


game_status(0, 0, True)


def human_add(zombies_wins, humans_wins):
    if humans_wins - zombies_wins > 10:      # (t, p)
        humans.append(choices(range(min_coordinate, max_coordinate), k=3))
        return print(f"Ludzie rosną w siłę, przybył nowy gracz {humans[-1]}")


def main():
    iteration = 1
    game_in_progress = True
    zombies_wins = 0
    humans_wins = 0

    while game_in_progress:
        for index_z, zombi_pos in enumerate(zombies):
            for index_h, humen_pos in enumerate(humans):
                distance = int(sqrt((zombi_pos[0] - humen_pos[0]) ** 2 + (zombi_pos[1] - humen_pos[1]) ** 2))
                if distance > 0:
                    distance -= 1
                else:
                    distance += 1
                print(f"\n Iteracja numer {iteration}")
                if distance <= min_distance:
                    print(f"Walka zombi:{zombi_pos} - człowiek:{humen_pos}, dystans:{distance}")
                    if zombi_pos[2] > humen_pos[2]:     # Zombi silniejszy od człowieka
                        zombi_pos[2] -= humen_pos[2]
                        zombies.append(humen_pos)       # Pokonany człowiek dodany do zombi
                        humans.pop(index_h)             # Pokonany człowiek usunięty z ludzi
                        zombies_wins += 1
                        print(f"Ludzie -1")
                        print(f"Zombi power -{humen_pos[2]} : {zombi_pos}")
                        human_add(zombies_wins, humans_wins)
                        game_in_progress = game_status(zombies_wins, humans_wins, game_in_progress)
                        break
                    if zombi_pos[2] < humen_pos[2]:    # Zombi słabszy od człowieka
                        humen_pos[2] -= zombi_pos[2]
                        zombies.pop(index_z)
                        humans_wins += 1
                        print(f"Zombi -1")
                        print(f"Człowiek power -{zombi_pos[2]} : {humen_pos}")
                        human_add(zombies_wins, humans_wins)
                        game_in_progress = game_status(zombies_wins, humans_wins, game_in_progress)
                        break
                    if zombi_pos[2] == humen_pos[2]:  # Człowiek i zombi na równi silni
                        print(f"Remis -  Zombi i Ludzie -1")
                        zombies.pop(index_z)
                        humans.pop(index_h)
                        human_add(zombies_wins, humans_wins)
                        game_in_progress = game_status(zombies_wins, humans_wins, game_in_progress)
                        break

                elif distance > min_distance:
                    # humans.append(choices(range(min_coordinate, max_coordinate), k=3))
                    # zombies.append(choices(range(min_coordinate, max_coordinate), k=3))
                    # print(f"Dodano człowieka: {humans[-1]}")
                    # print(f"Dodano zombi: {zombies[-1]}")
                    print(f"Zombi {zombies[index_z]}")
                    if zombi_pos[0] > 0:
                        zombi_pos[0] -= 1
                    else:
                        zombi_pos[0] += 1
                    if zombi_pos[1] > 0:
                        zombi_pos[1] -= 1
                    else:
                        zombi_pos[1] += 1
                    print(f"zmienił swoją pozycję: {zombies[index_z]}")
                    break

        iteration += 1

if __name__ == "__main__":
    main()
