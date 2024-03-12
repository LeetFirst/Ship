import pygame
import sys
from settings import Settings
from ship import Ship



class SpaceInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))

        self.rect = self.screen.get_rect() 
        self.ship = Ship(self)



    def _check_key_down(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_a:
            self.ship.flagLeft = True

        elif event.key == pygame.K_d:
            self.ship.flagRight = True



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


    def run_game(self):
        while True:
            self.screen.fill(self.setting.color)
            self._check_event()
            self.ship.update()
            pygame.display.flip()

            

               


if __name__ == '__main__':
    GAME = SpaceInvasion()
    GAME.run_game()


