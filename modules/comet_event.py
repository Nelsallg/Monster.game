import pygame
from modules.comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.all_comets = pygame.sprite.Group()
        self.game = game

    def increment_percent(self):
        self.percent += self.percent_speed / 100
        # self.update_comet_bar(surface)

    def is_fulled_comet_bar(self):
        return self.percent >= 100

    def reset_comet_bar(self):
        self.percent = 0

    def comets_falling(self):
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_fulled_comet_bar():
            print("pluie de comet")
            self.comets_falling()
            self.reset_comet_bar()

    def update_comet_bar(self, surface) -> None:
        self.increment_percent()
        self.attempt_fall()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 15])
        pygame.draw.rect(surface, (241, 33, 33), [
            0, surface.get_height() - 20,
            surface.get_width() / 100 * self.percent, 15])
