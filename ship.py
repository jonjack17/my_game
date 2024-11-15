import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, sr_game):
        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings

        self.image = pygame.image.load('images/ship5.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # self.moving_right = False
        # self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += self.settings.ship_speed
        # if self.moving_left and self.rect.left > 0:
        #     self.x -= self.settings.ship_speed
        
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft


    def blitme(self):
        self.screen.blit(self.image, self.rect)