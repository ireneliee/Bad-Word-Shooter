import pygame

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


class Bullet(pygame.sprite.Sprite):
    def __init__ (self, coorX, coorY, bullet_img):
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
