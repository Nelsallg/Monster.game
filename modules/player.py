import pygame
from modules.projectile import Projectile
from animations.animation import AnimateSprite


# Creer une class qui represente le joueur
class Player(AnimateSprite):
    def __init__(self, game) -> None:
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health > 0:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self) -> None:
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        self.animation_start()

    def update_health_bar(self, surface) -> None:
        bar_green_color = (111, 210, 46)
        if self.health <= 50:
            bar_green_color = (254, 194, 65)
        if self.health <= 25:
            bar_green_color = (241, 33, 33)
        bar_background_color = (60, 63, 60)
        bar_position = [self.rect.x + 50, self.rect.y, self.health, 10]
        bar_background_position = [self.rect.x + 50, self.rect.y, self.max_health, 10]
        pygame.draw.rect(surface, bar_background_color, bar_background_position)
        pygame.draw.rect(surface, bar_green_color, bar_position)

    def update_animation(self):
        self.animate()

    def move_right(self) -> None:
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self) -> None:
        self.rect.x -= self.velocity
