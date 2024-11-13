import pygame
from pygame.sprite import Sprite
from random import randint

# A class to manage raindrops. Raindrops should move top to bottom in a grid
# format. When one row reaches the bottom of the screen, another row should
#  appear at the top of the screen and begin to fall. The position of each row 
# should be slightly randomized to create a realistic appearance.

class Raindrop(Sprite):

    def __init__(self, sr_game):
        """A class to manage raindrops."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.color = self.settings.raindrop_color

        self.rect = pygame.Rect(0,0, self.settings.raindrop_width, 
                                self.settings.raindrop_height)
        
        
        self.y = float(self.rect.y)
    
    def update(self):
        """Drop the raindrop across the screen to the bottom"""
        random_number = randint(-3,3)
        self.y +=self.settings.raindrop_speed + random_number
        self.rect.y = self.y


    def draw_raindrop(self):
        """Draw the raindrop to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


    