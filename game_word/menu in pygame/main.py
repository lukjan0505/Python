import pygame
import button

pygame.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
menu_state = "main"

# define fonts
text_font = pygame.font.SysFont(None, 40, bold=True)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
new_img = pygame.image.load("images/button_new_game.png").convert_alpha()
dashboard_img = pygame.image.load("images/button_dashboard.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
one_player_img = pygame.image.load('images/button_one_player.png').convert_alpha()
two_players_img = pygame.image.load('images/button_two_players.png').convert_alpha()
results_img = pygame.image.load('images/button_results.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

# create button instances
new_button = button.Button(290, 125, new_img, 1)
dashboard_button = button.Button(248, 250, dashboard_img, 1)
quit_button = button.Button(300, 375, quit_img, 1)
one_player_button = button.Button(300, 75, one_player_img, 1)
two_players_button = button.Button(300, 200, two_players_img, 1)
results_button = button.Button(300, 450, results_img, 1)
back_button = button.Button(300, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:
    screen.fill((140, 170, 188))
    # Main menu
    if menu_state == "main":
        if new_button.draw(screen):
            menu_state = "new"
        if dashboard_button.draw(screen):
            menu_state = "dashboard"
        if quit_button.draw(screen):
            run = False
    # Menu new game
    if menu_state == "new":
        if one_player_button.draw(screen):
            menu_state = "one"
        if two_players_button.draw(screen):
            menu_state = "two"
        if back_button.draw(screen):
            menu_state = "main"
    # Menu new game
    if menu_state == "one":
        draw_text("Gra dla 1 osoby", text_font, (0, 0, 0), 220, 150)
        if back_button.draw(screen):
            menu_state = "new"
    if menu_state == "two":
        draw_text("Gra dla 2 osób", text_font, (0, 0, 0), 220, 150)
        if back_button.draw(screen):
            menu_state = "new"
    # Menu dashboard
    if menu_state == "dashboard":
        print("Tabela wyników")
        if results_button.draw(screen):
            print("Wyniki")
        if back_button.draw(screen):
            menu_state = "main"

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
