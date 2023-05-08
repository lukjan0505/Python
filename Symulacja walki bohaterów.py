from random import choices, randint


class Superhero:
    def __init__(self):
        self.hero = choices(('Sub-Zero', 'Scorpion', 'Liu Kang', 'Kung Lao', 'Sonya', 'Johnny Cage', 'Raiden', 'Jax'))
        self.superpower = choices(('lava rain', 'water attack', 'power ball storm', 'dragging underground',
                                   'crushing into the ground', 'laser vision', 'gust of power'))
        self.life_points = randint(1, 10)

    def info(self):
        print("Bohater: " + "".join(self.hero))
        print("Super moc: " + "".join(self.superpower))
        print("Życie: " + "".join(str(self.life_points)))

    def decrease_life(self, h1_attack, h2_attack):
        if h1_attack > h2_attack:
            self.life_points = self.life_points - (h1_attack - h2_attack)
        elif h2_attack > h1_attack:
            self.life_points = self.life_points - (h2_attack - h1_attack)


def attack():
    return randint(1, 10)


def end_game(game_in_progress2=True):
    if hero1.life_points <= 0:
        print("Wygrał gracz: ", '\x1b[38;2;255;255;255m\x1b[48;2;0;0;255m' + " ".join(hero2.hero) + '\x1b[0m')
        game_in_progress2 = False
    elif hero2.life_points <= 0:
        print("Wygrał gracz: ", '\x1b[38;2;255;255;255m\x1b[48;2;0;0;255m' + " ".join(hero1.hero) + '\x1b[0m')
        game_in_progress2 = False
    return game_in_progress2


hero1 = Superhero()
hero2 = Superhero()
hero1.info()
hero2.info()
print("------")
game_in_progress = True
while game_in_progress:
    hero1_attack = attack()
    hero2_attack = attack()
    if hero1.hero == hero2.hero:
        hero2.hero = "".join(hero2.hero) + ' (cień)'
        print('\x1b[38;2;255;0;0m\x1b[48;2;255;255;255m' + 'Emocjonująca walka z własnym cieniem!' + '\x1b[0m')
    if hero1_attack > hero2_attack:
        print(f"Gracz " + "".join(hero1.hero) + f", życie: {hero1.life_points}, "
              f"atakuje z mocą: {hero1_attack} i miażdży przeciwnika supermocą: "+"".join(hero1.superpower))
        print(f"Gracz " + "".join(hero2.hero) + f", życie: {hero2.life_points}, "
              f"atak: {hero2_attack}, traci: {hero1_attack - hero2_attack} punktów życia")
        hero2.life_points -= (hero1_attack - hero2_attack)
        print("------")
        game_in_progress = end_game()
    elif hero1_attack < hero2_attack:
        print(f"Gracz " + "".join(hero2.hero) + f", życie: {hero2.life_points}, "
              f"atakuje z mocą: {hero2_attack} i miażdży przeciwnika supermocą: "+"".join(hero2.superpower))
        print(f"Gracz " + "".join(hero1.hero) + f", życie: {hero1.life_points}, "
              f"atak: {hero1_attack}, traci: {hero2_attack - hero1_attack} punktów życia")
        hero1.life_points -= (hero2_attack - hero1_attack)
        print("------")
        game_in_progress = end_game()
    else:
        print("Gracze zaatakowali z tą samą mocą. Nikt nie traci punktów życia.")
        print("------")
        game_in_progress = end_game()

hero1.info()
hero2.info()
