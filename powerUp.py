import pygame
import random

#window setting
WIDTH = 480
HEIGHT = 600
FPS = 60

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