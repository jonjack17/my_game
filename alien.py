import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """A class to represent a single alien in the fleet."""
    def __init__(self, sr_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/Nave.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen
        # self.rect.x = self.settings.screen_width - self.rect.width
        # self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien left towards the player"""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
