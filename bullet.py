import pygame
from pygame.sprite import Sprite

# A file to manage bullets. Bullets must travel left to right, and must be 
# deleted when they leave the screen. A maximum of 4 bullets can be on 
# screen at any one point in time.

# Bullet rect must be created. the rect must be displayed. the position must 
# be updated and redrawn to the screen

class Bullet(Sprite):
    """A class to manage bullets."""

    def __init__(self, sr_game):
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set its position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midright = sr_game.ship.rect.midright

        # Store the bullets position as a float
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen"""
        # Update the exact position of the bullet
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

