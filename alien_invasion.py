import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings      = Settings()
        self.bg_image      = pygame.image.load(self.settings.bg_image)
        self.screen        = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width  = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
    

    def _check_events(self):
        for event in pygame.event.get():   
               
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self.check_key_down_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_key_up_events(event)

    def check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_rigth = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_rigth = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """ Vai atualizar o ecrã """
        self.screen.blit(self.bg_image, (0,0))
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()
    
              
            
if __name__ == '__main__':
    
    jogo = AlienInvasion()
    jogo.run()










