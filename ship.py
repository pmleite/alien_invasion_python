import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen         = ai_game.screen
        self.screen_rect    = ai_game.screen.get_rect()
        self.image          = pygame.image.load(ai_game.settings.ship_image)
        self.rect           = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x              = float(self.rect.x)
        self.moving_right   = False
        self.moving_left    = False

    def update(self, ai_game):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += ai_game.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= ai_game.settings.ship_speed 

        self.rect.x = self.x  

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x              = float(self.rect.x)


