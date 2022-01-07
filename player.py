import pygame
from color import Color
from windowSetting import WindowSetting

WIDTH = 480
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(WindowSetting.GREEN)
        self.speedx = 0
        self.speedy = 0
        self.rect = self.image.get_rect()
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

