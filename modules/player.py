import pygame
     
#Creer une class qui represente le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__
        self.health = 100
        self.max_health = 100
        self.attck = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def move_right(self) -> None:
        self.rect.x += self.velocity
    def move_left(self) -> None:
        self.rect.x -= self.velocity
