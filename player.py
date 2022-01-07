import pygame
from bullet import Bullet

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

class Player(pygame.sprite.Sprite):
    def __init__(self, spaceship_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spaceship_img, (75,57))
        self.speedx = 0
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
    
    def update(self):
        # timeout for power ups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWEREUP_TIME:
            self.power -= 2
            self.power_time = pygame.time.get_ticks()
        
        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] :
            self.speedx = -10
        
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def shoot(self, all_sprites, bullets, bullet_img, shoot_sound):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now

            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery, bullet_img)
                bullet2 = Bullet(self.rect.right, self.rect.centery, bullet_img)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            else:
                bullet = Bullet(self.rect.centerx, self.rect.top, bullet_img)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
        
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)
