from modules.player import Player
from modules.monster import Monster
import pygame
import random
#Creer une seconde class qui represente le joueur
class Game():
    def __init__(self) -> None:
        #Generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #Groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        for i in range(random.randint(1,10)):
            if i % 2 == 0:
                self.spawn_monster()
      
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
