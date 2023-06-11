import pygame
from modules.game import Game

pygame.init()

#Gerer la fenetre
pygame.display.set_caption("Monster")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('assets/images/bg.jpg')

#Charger le joueur
game = Game()

running = True
while running:
    #Executer la fenetre de jeu
    screen.blit(background, (0,-200))
    
    #Appliquer l'image  du joueur
    screen.blit(game.player.image, game.player.rect)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la fenetre en cours...")
        #detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right
            elif event.key == pygame.K_LEFT:
                game.player.move_left