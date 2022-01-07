import pygame
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

other_img_dir = path.join(path.dirname(__file__),"other_image_folder")
bullet_img = pygame.image.load(path.join(other_img_dir,"laserblue.png"))

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, coorX, coorY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (10, 38))
        self.rect = self.image.get_rect()
        self.rect.bottom = coorY
        self.rect.centerx = coorX
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
