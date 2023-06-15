import pygame


def resize(image, screen):
    max_width = screen.get_width()
    max_height = screen.get_height()

    original_width, original_height = image.get_size()

    # Vérifiez si l'image doit être redimensionnée
    if original_width > max_width or original_height > max_height:
        # Calculez le facteur d'échelle pour ajuster l'image à la taille maximale tout en conservant le ratio d'aspect
        scale_factor = min(max_width / original_width, max_height / original_height)

        # Redimensionnez l'image avec le facteur d'échelle
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        resized_image = pygame.transform.scale(image, (new_width, new_height))

        return resized_image
    return image
