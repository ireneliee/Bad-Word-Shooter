import pygame
from player import Player
from mob import Mob
from os import path 

#window setting
WIDTH = 480
HEIGHT = 600
FPS = 60

#color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#Initialise pygame and create window
pygame.init()
#Enable sound effects in game
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Set the caption of the screen
pygame.display.set_caption("Bad Words Shooter!")


clock = pygame.time.Clock()
#Set speed of the game
clock = pygame.time.Clock()
#Place all sprites into a group

font_name = pygame.font.match_font('Halvetica')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop(x, y)
    surf.blit(text_surface, text_rect)

other_img_dir = path.join(path.dirname(__file__),"other_image_folder")
background = pygame.image.load(path.join(other_img_dir, "background.png")).convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group()

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
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot(all_sprites, bullets)
    #Update
    all_sprites.update()

    #check if a bullet hits a meteor
    shots = pygame.sprite.groupcollide(meteors, bullets, True, True)

    #respawn meteors so we won't run out
    for shot in shots:
        meteor = Mob()
        all_sprites.add(meteor)
        meteors.add(meteor)

    #kills the spaceshit when meteor hits spaceship
    hits = pygame.sprite.spritecollide(spaceship, meteors, False)
    if hits:
        running = False

    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
#Close the game
pygame.quit()



