import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/images/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 100
            self.velocity = random.randint(1, 3)
            self.rect.x = 1000 + random.randint(0, 300)

    def update_health_bar(self,surface) -> None:
        bar_green_color = (111,210,46)
        if self.health <= 50:
            bar_green_color = (254,194,65)
        if self.health <= 25:
            bar_green_color = (241, 33, 33)
        bar_background_color = (60,63,60)
        bar_position = [self.rect.x + 10,self.rect.y - 20,self.health,5]
        bar_background_position = [self.rect.x + 10,self.rect.y - 20,self.max_health,5]
        pygame.draw.rect(surface, bar_background_color, bar_background_position)
        pygame.draw.rect(surface, bar_green_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
          
    def zombie_arme(self):
        self.image = pygame.image.load('assets/images/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def clown(self):
        self.image = pygame.image.load('assets/images/clown.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def killer_1(self):
        self.image = pygame.image.load('assets/images/killer_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        
    def killer_2(self):
        self.image = pygame.image.load('assets/images/killer_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500