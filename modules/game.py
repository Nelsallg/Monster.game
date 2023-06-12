from modules.player import Player
from modules.monster import Monster
import pygame
import random
from modules.comet_event import CometFallEvent


# Creer une seconde class qui represente le joueur
class Game():
    def __init__(self) -> None:
        self.is_starting = False
        # Generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.comet_event = CometFallEvent(self)

    def generate_random_spawn_monster(self):
        for i in range(random.randint(1, 10)):
            if i % 2 == 0:
                self.spawn_monster()

    def game_start(self):
        self.is_starting = True
        self.generate_random_spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_starting = False

    def update(self, screen):
        # Insérer l'image du joueur dans la fenetre de jeu
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)
        self.comet_event.update_comet_bar(screen)

        # Gestion du deplacement des projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Gestion du deplacement des monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for comet in self.comet_event.all_comets:
            comet.fall()

        # Dessiner les assets sur l'ecran
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_event.all_comets.draw(screen)


        # Gestion des déplacements du joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
