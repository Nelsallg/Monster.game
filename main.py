import pygame
from modules.game import Game

pygame.init()

#Gérer les propriétés de la fenetre de jeu
pygame.display.set_caption("Monster")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('assets/images/bg.jpg')

#créer une instance de la class Game
game = Game()

running = True
while running:
    #Appliquer le background à la fenetre de jeu
    screen.blit(background, (0,-200))
    
    #Insérer l'image du joueur dans la fenetre de jeu
    screen.blit(game.player.image, game.player.rect)

    game.player.update_health_bar(screen)

    #Gestion du deplacement des projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #Gestion du deplacement des monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
    
    #Dessiner les assets sur l'ecran
    game.player.all_projectiles.draw(screen)
    game.all_monsters.draw(screen)
    
    #Gestion des déplacements du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        
    
    pygame.display.flip()
    for event in pygame.event.get():
        #Gestion des évènements
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la fenetre en cours...")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False