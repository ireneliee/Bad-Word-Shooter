import pygame
from color import Color
from windowSetting import WindowSetting

WIDTH = 480
HEIGHT = 600

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, coorX, coorY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(Color.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = coorY
        self.rect.centerx = coorX
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
