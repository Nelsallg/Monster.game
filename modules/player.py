import pygame
from modules.projectile import Projectile
     
#Creer une class qui represente le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        super().__init__
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def launch_projectile(self) -> None:
        self.all_projectiles.add(Projectile(self))
        
    def move_right(self) -> None:
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
        
    def move_left(self) -> None:
        self.rect.x -= self.velocity
