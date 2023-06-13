import pygame
import time


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name: str):
        super().__init__()
        self.image = pygame.image.load(f'assets/images/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.last_frame_time = time.time()
        self.animation = False

    def animation_start(self):
        self.animation = True

    def animate(self, frame_delay: int = None, loop=False):
        if self.animation:
            current_time = time.time()
            if frame_delay is not None:
                while current_time - self.last_frame_time < frame_delay / 100:
                    current_time = time.time()

            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]
            self.last_frame_time = current_time


def load_animation_images(sprite_name):
    images = []
    path = f'assets/images/{sprite_name}/{sprite_name}'
    for i in range(1, 24):
        image_path = path + str(i) + '.png'
        images.append(pygame.image.load(image_path))
    return images


animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}
