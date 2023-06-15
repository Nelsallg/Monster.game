import pygame
import random
from tools.screen import replace_by_viewheight


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/images/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(5, 15)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_comet_bar()
            self.comet_event.game.generate_random_spawn_monster()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= replace_by_viewheight(220):
            self.remove()
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)
