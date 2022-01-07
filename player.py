import pygame
from color import Color
from windowSetting import WindowSetting
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(Color.GREEN)
        self.speedx = 0
        self.speedy = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = WindowSetting.WIDTH / 2
        self.rect.bottom = WindowSetting.HEIGHT - 10
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

        if self.rect.right > WindowSetting.WIDTH:
            self.rect.right = WindowSetting.WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

