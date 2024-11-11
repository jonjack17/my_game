import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    """A class to manage background stars."""
    def __init__(self, sr_game):
        """Initialize a star and set its position."""
        super().__init__()

        self.settings = sr_game.settings
        self.screen = sr_game.screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

      





        