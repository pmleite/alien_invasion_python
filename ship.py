import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Flag
        self.moving_rigth = False
        self.moving_left = False

    def update(self):
        if (self.moving_rigth) and (self.rect.right < self.screen_rect.right):
            self.rect.x += 1
        if (self.moving_left) and (self.rect.left > 0):
            self.rect.x -= 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)


