import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player) -> None:
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/images/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        #self.comet_event = CometFallEvent()

    def rotate(self) -> None:
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self) -> None:
        self.player.all_projectiles.remove(self)

    def move(self) -> None:
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)
            #self.comet_event.increment_percent(screen)
        if self.rect.x > 1080:
            self.remove()
