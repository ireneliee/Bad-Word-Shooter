import pygame
import random

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


class GoodMob(pygame.sprite.Sprite):
    def __init__ (self, meteor_images):
        pygame.sprite.Sprite.__init__(self)
        meteor_img = random.choice(meteor_images)

        sizex = random.randrange(100, 160)
        sizey = sizex

        if(meteor_img.get_rect().width < 300):
            sizex = meteor_img.get_rect().width
            sizey = meteor_img.get_rect().height

        self.image = pygame.transform.scale(meteor_img, (sizex, sizey))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3, 3)


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, 40)
            self.speedy = random.randrange(1, 8)
