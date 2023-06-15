import pygame
from modules.game import Game
import math
import modules.image_resizer as ImageResizer
from sys import exit
from settings.settings import *


# Gérer les propriétés de la fenetre de jeu
pygame.display.set_caption("Monster")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = ImageResizer.resize(pygame.image.load('assets/images/bg_1080x617_bg_on_boat_night.jpg'), screen)

# Gestion de la banniere
banner = pygame.image.load('assets/images/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_height = banner.get_height()
# Gestion du boutton play
play_button = pygame.image.load('assets/images/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# créer une instance de la class Game
game = Game()

running = True
while running:
    # Appliquer le background à la fenetre de jeu
    screen.blit(background, (0, 0))

    if game.is_starting:
        game.update(screen)
    else:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner, (banner_rect.x, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        # Gestion des évènements
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la fenetre en cours...")
            exit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.game_start()
    clock.tick(FPS)
