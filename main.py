import pygame
import random

#Constant for Screen Width, Height and FPS
WIDTH = 480
HEIGHT = 600
FPS = 60

#Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Initialise pygame and create window
pygame.init()
#Enable sound effects in game
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Set the caption of the screen
pygame.display.set_caption("My Game")
#Set speed of the game
clock = pygame.time.Clock()
#Place all sprites into a group
all_sprites = pygame.sprite.Group()

#Game loop
running = True
while running:
    #Keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Draw / Render
    screen.fill(BLACK)
    #Blit the sprites images
    all_sprites.draw(screen)
    pygame.display.flip()
#Close the game
pygame.quit()



