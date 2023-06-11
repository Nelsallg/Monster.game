import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load('assets/images/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
          
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