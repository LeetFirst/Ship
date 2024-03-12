import pygame
from settings import Settings

class Ship:

    def __init__(self, gameClass):
        self.screen  = gameClass.screen
        self.screen_rect = gameClass.rect

        self.setting = Settings()

        self.image = pygame.image.load('image/ship.bmp')

        self.rect_image = self.image.get_rect()


        self.rect_image.midbottom = self.screen_rect.midbottom

        self.flagRight = False
        self.flagLeft = False



    def mov_ship(self):
        if self.flagLeft and self.rect_image.x >= self.screen_rect.left:
            self.rect_image.x -= self.setting.ship_speed
           
        if self.flagRight and self.rect_image.x <= (self.screen_rect.right - self.rect_image.width):
            self.rect_image.x += self.setting.ship_speed
            
        
    
    def update(self):
        self.mov_ship()
        self.screen.blit(self.image, self.rect_image)





