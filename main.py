import pygame
import random
from player import Player
from mob import Mob
from color import Color
from windowSetting import WindowSetting

#Initialise pygame and create window
pygame.init()
#Enable sound effects in game
pygame.mixer.init()
screen = pygame.display.set_mode((WindowSetting.WIDTH, WindowSetting.HEIGHT))
#Set the caption of the screen
pygame.display.set_caption("Bad Words Shooter!")
#Set speed of the game
clock = pygame.time.Clock()
#Place all sprites into a group
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()

spaceship = Player()
all_sprites.add(spaceship)


for i in range(8):
    meteor = Mob()
    all_sprites.add(meteor)
    meteors.add(meteor)


#Game loop
running = True
while running:
    #Keep loop running at the right speed
    clock.tick(WindowSetting.FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Draw / Render
    screen.fill(WindowSetting.BLACK)
    #Blit the sprites images
    all_sprites.draw(screen)
    pygame.display.flip()
#Close the game
pygame.quit()



