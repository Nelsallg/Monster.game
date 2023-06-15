import pygame

surface = pygame.display.get_surface()


def replace_monster_on_width():
    if surface:
        width = surface.get_width()
        return width
    return 1080


def replace_by_viewheight(value):
    if surface:
        height = surface.get_height()
        return height - value
    return 617 - value
