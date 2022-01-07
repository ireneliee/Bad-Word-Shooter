import pygame
import random
from player import Player
from mob import Mob
from explosion import Explosion
from os import path 
from powerUp import PowerUp
from goodMob import GoodMob

#window setting
WIDTH = 1200
HEIGHT = 700
FPS = 60
POWEREUP_TIME = 5000

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

font_name = pygame.font.match_font('arial')

def show_starting_screen():
    draw_text(screen, "BAD WORDS SHOOTER!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys to move, Space to fire", 44, WIDTH/2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 35, WIDTH / 2, HEIGHT * 3 / 4 )
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def create_shield_bar(surf, x, y, health):
    if health < 0:
        health = 0
    BAR_WIDTH = 200
    BAR_HEIGHT = 10
    fill = (health / 100) * BAR_WIDTH
    rect_outside = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    rect_inside = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, rect_inside)
    pygame.draw.rect(surf, WHITE, rect_outside, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

# finding the right folder
other_img_dir = path.join(path.dirname(__file__),"other_image_folder")
bad_img_dir = path.join(path.dirname(__file__),"bad_image_folder")
good_img_dir = path.join(path.dirname(__file__),"good_image_folder")
sound_dir = path.join(path.dirname(__file__), "sound_folder")
explosion_dir = path.join(path.dirname(__file__), "explosion_image_folder")

# adding the resources file into the game
spaceship_img = pygame.image.load(path.join(other_img_dir, "spaceship.png")).convert_alpha()
spaceship_mini_img = pygame.transform.scale(spaceship_img, (25, 19)).convert_alpha()
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

asteroid_images = []
asteroid_list = ['asteroid1.png', 'asteroid2.png', 'asteroid3.png', 'asteroid4.png', 'asteroid5.png',
 'asteroid6.png', 'asteroid7.png', 'asteroid8.png', 'asteroid9.png', 'asteroid10.png', 'asteroid11.png',
  'asteroid12.png', 'asteroid13.png', 'asteroid14.png', 'asteroid15.png', 'asteroid16.png', 'asteroid17.png',
   'asteroid18.png', 'asteroid19.png', 'asteroid20.png']

for image in asteroid_list:
    asteroid_img = pygame.image.load(path.join(good_img_dir, image)).convert_alpha()
    asteroid_images.append(asteroid_img)

explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(explosion_dir, filename)).convert_alpha()
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)
    filename_person = "sonicExplosion0{}.png".format(i)
    person_exp_img = pygame.image.load(path.join(explosion_dir, filename_person)).convert_alpha()
    explosion_anim["player"].append(img)

powerup_images = {}
shield_file = pygame.image.load(path.join(other_img_dir, 'powerupRed_shield.png')).convert_alpha()
bolt_file = pygame.image.load(path.join(other_img_dir, 'powerupYellow_bolt.png')).convert_alpha()
powerup_images["shield"] = shield_file
powerup_images["gun"] = bolt_file


def newMeteor(level):
    meteor = Mob(meteor_images, level)
    all_sprites.add(meteor)
    meteors.add(meteor)

def newAsteroid(level):
    asteroid = GoodMob(asteroid_images, level)
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

shoot_sound = pygame.mixer.Sound(path.join(sound_dir, "laser.wav"))
shield_sound = pygame.mixer.Sound(path.join(sound_dir, "shield.wav"))
power_sound = pygame.mixer.Sound(path.join(sound_dir, "gun.wav"))
explosion_sound = []
explosion_list = ["explosion1.wav", "explosion2.wav"]

for snd in explosion_list:
    sound = pygame.mixer.Sound(path.join(sound_dir, snd))
    explosion_sound.append(sound)
die_sound = pygame.mixer.Sound(path.join(sound_dir, "rumble1.ogg"))
pygame.mixer.music.load(path.join(sound_dir, "gameover.ogg"))   
pygame.mixer.music.set_volume(0.1)

pygame.mixer.music.play(10)

#Game loop
game_over = True
running = True
while running:
    if game_over:
        screen.blit(background, background_rect)
        show_starting_screen()
        game_over = False
        
        all_sprites = pygame.sprite.Group()
        meteors = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite .Group() 
        asteroids = pygame.sprite.Group()

        spaceship = Player(spaceship_img)
        all_sprites.add(spaceship)

        score = 0
        level = int(score / 1000)
        if level == 0:
            level = 1

        for i in range(3):
            newMeteor(level)
            newAsteroid(level)

        
    #Keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot(all_sprites, bullets, bullet_img, shoot_sound)
    
    #Update
    all_sprites.update()
    
    #check if a bullet hits a meteor
    meteorShots = pygame.sprite.groupcollide(meteors, bullets, True, True)

    #respawn meteors so we won't run out
    for shot in meteorShots:
        score = score + (200 - shot.radius)
        random.choice(explosion_sound).play()
        random.choice(explosion_sound).play()
        expl = Explosion(shot.rect.center, 'lg', explosion_anim)
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = PowerUp(shot.rect.center, powerup_images)
            all_sprites.add(pow)
            powerups.add(pow)

        level = int(score / 1000)
        if level == 0:
            level = 1
        newMeteor(level)
    
    asteroidShots = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for shot in asteroidShots:
        score = score - shot.radius
        random.choice(explosion_sound).play()
        random.choice(explosion_sound).play()
        expl = Explosion(shot.rect.center, 'lg', explosion_anim)
        all_sprites.add(expl)
        level = int(score / 1000)
        if level == 0:
            level = 1
        newAsteroid(level)
 
    #kills the spaceshit when meteor hits spaceship
    hits = pygame.sprite.spritecollide(spaceship, meteors, True, pygame.sprite.collide_circle)
    for hit in hits:
        spaceship.shield -= hit.radius * 1
        random.choice(explosion_sound).play()
        expl = Explosion(hit.rect.center, 'sm', explosion_anim)
        all_sprites.add(expl)
        level = int(score / 1000)
        if level == 0:
            level = 1
        newMeteor(level)
        if spaceship.shield < 0:
            die_sound.play()
            player_explosion = Explosion(spaceship.rect.center, "player", explosion_anim)
            all_sprites.add(player_explosion)
            spaceship.hide()
            spaceship.lives -= 1
            spaceship.shield = 100
            

    hitsPowerUp = pygame.sprite.spritecollide(spaceship, powerups, True)
    for hit in hitsPowerUp:
        if hit.type == "shield":
            shield_sound.play()
            spaceship.shield += random.randrange(30, 50)
            if spaceship.shield >= 100:
                spaceship.shield = 100
            
        elif hit.type == "gun":
            power_sound.play()
            spaceship.powerup()

    if spaceship.lives <= 0:
                running = False

    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 36,  WIDTH/2, 10)
    create_shield_bar(screen, 5, 5, spaceship.shield)
    draw_lives(screen, WIDTH - 100, 5, spaceship.lives, spaceship_mini_img)
    pygame.display.flip() 
#Close the game
pygame.quit()



