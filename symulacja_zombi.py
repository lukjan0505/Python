"""
Symulacja walki ludzi z zombi.

Liczba par -losowa z przedziału (2, 15).
Parametry człowieka i zombi:
    (x, y, s) - człowiek/zombi
    x -położenie na osi x
    y -położenie na osi y
    s -siła

    W walce biorą udział pary człowiek-zombi, pomiędzy którymi odległość jest większa, równa 3.
    Jeżeli nie ma takiej pary, dodawane jest do list po jednym zawodniku, aż warunek odległości będzie spełniony.
    Siła zwycięskiego osobnika po wygranej jest pomniejszana o siłę pokonanego.
    Zwycięzca przechodzi do następnej rundy.
    Przegrywa grupa, która zostaje całkowicie wyeliminowana.


"""
from random import choices, randrange
from math import sqrt
min_distance = 3
number_of_players = randrange(2, 15)
min_coordinate = 1
max_coordinate = 10
humans = [list(choices(range(min_coordinate, max_coordinate), k=3)) for humen in range(number_of_players)]
zombies = [list(choices(range(min_coordinate, max_coordinate), k=3)) for zombi in range(number_of_players)]
print(f"Liczba par: {len(humans)}")


def game_status():
    print(f"Ludzie: {len(humans)}, Zombi: {len(zombies)}")
    print(f"Zombi: {zombies}")
    print(f"Ludzie: {humans} \n")


game_status()

# def win_status(z, h, game_in_progress): ---------Nie działa jak trzeba - wpada w nieskończoną pętlę
#     if z == 0:
#         print(f"Ludzie wygrali bitwę {len(humans)} do {len(zombies)}!")
#         game_in_progress = False
#     if h == 0:
#         print(f"Zombie wygrały bitwę {len(zombies)} do {len(humans)}!")
#         game_in_progress = False
#     if len(zombies) > len(humans) == 0:
#         print(f"Remis!")
#         game_in_progress = False
#     else:
#         return game_in_progress
#     return game_in_progress


def main():
    iteration = 1
    game_in_progress = True

    while game_in_progress:
        print(f"\n Iteracja numer {iteration}")
        for index_z, zombi_pos in enumerate(zombies):
            for index_h, humen_pos in enumerate(humans):
                distance = int(sqrt((zombi_pos[0] - humen_pos[0]) ** 2 + (zombi_pos[1] - humen_pos[1]) ** 2))
                if distance <= min_distance:
                    print(f"Walka zombi:{zombi_pos} - człowiek:{humen_pos}, dystans:{distance}")
                    if zombi_pos[2] > humen_pos[2]:
                        zombi_pos[2] -= humen_pos[2]
                        humans.pop(index_h)
                        print(f"Ludzie -1")
                        print(f"Zombi power -{humen_pos[2]} : {zombi_pos}")
                        game_status()
                        # win_status(len(zombies), len(humans), game_in_progress)
                        if len(humans) == 0:
                            print(f"Zombie wygrały bitwę {len(zombies)} do {len(humans)}!")
                            game_in_progress = False
                        break
                    elif zombi_pos[2] < humen_pos[2]:
                        humen_pos[2] -= zombi_pos[2]
                        zombies.pop(index_z)
                        print(f"Zombi -1")
                        print(f"Człowiek power -{zombi_pos[2]} : {humen_pos}")
                        game_status()
                        # win_status(len(zombies), len(humans), game_in_progress)
                        if len(zombies) == 0:
                            print(f"Ludzie wygrali bitwę {len(humans)} do {len(zombies)}!")
                            game_in_progress = False
                        break
                    elif zombi_pos[2] == humen_pos[2]:
                        print(f"Remis -  Zombi i Ludzie -1")
                        zombies.pop(index_z)
                        humans.pop(index_h)
                        game_status()
                        # win_status(len(zombies), len(humans), game_in_progress)
                        if len(zombies) == len(humans) == 0:
                            print(f"Remis!")
                            game_in_progress = False
                        break
                else:
                    humans.append(choices(range(min_coordinate, max_coordinate), k=3))
                    zombies.append(choices(range(min_coordinate, max_coordinate), k=3))
                    print(f"Dodano graczy! {humans[-1]}, {zombies[-1]}")
                    continue
        iteration += 1


if __name__ == "__main__":
    main()
