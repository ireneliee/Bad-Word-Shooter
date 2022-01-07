import pygame
import random

#window setting
WIDTH = 1200
HEIGHT = 700
FPS = 60
POWEREUP_TIME = 5000

class PowerUp(pygame.sprite.Sprite):
    def __init__ (self, center, powerup_images):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["shield", "gun"])
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()