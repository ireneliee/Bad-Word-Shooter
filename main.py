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

font_name = pygame.font.match_font('Monotype Corsiva')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# finding the right folder
other_img_dir = path.join(path.dirname(__file__),"other_image_folder")
bad_img_dir = path.join(path.dirname(__file__),"bad_image_folder")
sound_dir = path.join(path.dirname(__file__), "sound_folder")

# adding the resources file into the game
spaceship_img = pygame.image.load(path.join(other_img_dir, "spaceship.png")).convert_alpha()
bullet_img = pygame.image.load(path.join(other_img_dir, "laserblue.png")).convert_alpha()

background = pygame.image.load(path.join(other_img_dir, "background.png")).convert()
background_rect = background.get_rect()

meteor_images = []
meteor_list = ['meteor1.png', 'meteor2.png', 'meteor3.png', 'meteor4.png',
 'meteor6.png', 'meteor7.png', 'meteor8.png', 'meteor9.png',
  'meteor10.png', 'meteor11.png', 'meteor12.png', 'meteor13.png', 'meteor14.png',
   'meteor15.png', 'meteor16.png', 'meteor17.png', 'meteor18.png', 'meteor19.png',
    'meteor20.png', 'meteor21.png', 'meteor22.png', 'meteor23.png', 'meteor24.png',
     'meteor25.png', 'meteor26.png', 'meteor27.png', 'meteor28.png', 'meteor29.png',
      'meteor30.png', 'meteor31.png']

for image in meteor_list:
    meteor_img = pygame.image.load(path.join(bad_img_dir, image)).convert_alpha()
    meteor_images.append(meteor_img)

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group() 

spaceship = Player(spaceship_img)
all_sprites.add(spaceship)


for i in range(8):
    meteor = Mob(meteor_images)
    all_sprites.add(meteor)
    meteors.add(meteor)

score = 0

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
                spaceship.shoot(all_sprites, bullets, bullet_img)
    #Update
    all_sprites.update()

    #check if a bullet hits a meteor
    shots = pygame.sprite.groupcollide(meteors, bullets, True, True)

    #respawn meteors so we won't run out
    for shot in shots:
        score = score + (50 - shot.radius)
        meteor = Mob(meteor_images)
        all_sprites.add(meteor)
        meteors.add(meteor)
 
    #kills the spaceshit when meteor hits spaceship
    hits = pygame.sprite.spritecollide(spaceship, meteors, False)
    if hits:
        running = False

    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    pygame.display.flip()
#Close the game
pygame.quit()



