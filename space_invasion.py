import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet



class SpaceInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))

        self.rect = self.screen.get_rect() 
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()



    def _check_key_down(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_a:
            self.ship.flagLeft = True

        elif event.key == pygame.K_d:
            self.ship.flagRight = True
            
        elif event.key == pygame.K_SPACE and len(self.bullets) < 3:
            self.bullets.add(Bullet(self))




    def _check_key_up(self, event):
        if event.key == pygame.K_a:
            self.ship.flagLeft = False
        elif event.key == pygame.K_d:
            self.ship.flagRight = False


    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_key_down(event)
                if event.type == pygame.KEYUP:
                    self._check_key_up(event)


    def _mov_bullet(self):
        for bullet in self.bullets:
            if bullet.rect.y > -5:
                bullet.update()
                bullet.draw_bullet()
            else:
                self.bullets.remove(bullet)
        
    def run_game(self):
        while True: 
            self.screen.fill(self.setting.color)
            self._check_event()
            self.ship.update()
            self._mov_bullet()
            pygame.display.flip()

            

               


if __name__ == '__main__':
    GAME = SpaceInvasion()
    GAME.run_game()


