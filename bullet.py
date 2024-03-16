import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, gameClass):
        super().__init__()
        self.screen = gameClass.screen

        self.settings = gameClass.setting

        self.speed = self.settings.bullet_speed

        self.color = self.settings.color_bullet

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midbottom = gameClass.ship.rect_image.midtop

        self.rect.y = float(self.rect.y)

    def update(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

