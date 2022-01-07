import pygame
import random
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

bad_img_dir = path.join(path.dirname(__file__),"bad_image_folder")
meteor_img = pygame.image.load(path.join(bad_img_dir, "meteor1.png"))

class Mob(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteor_img, (100, 100))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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
