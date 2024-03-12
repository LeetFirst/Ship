import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, gameClass):
        super().__init__()