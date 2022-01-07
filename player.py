import pygame
from bullet import Bullet

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

class Player(pygame.sprite.Sprite):
    def __init__(self, spaceship_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spaceship_img, (50, 38))
        self.speedx = 0
        self.speedy = 0
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] :
            self.speedx = -5
        
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, all_sprites, bullets, bullet_img):
        bullet = Bullet(self.rect.centerx, self.rect.top, bullet_img)
        all_sprites.add(bullet)
        bullets.add(bullet)

