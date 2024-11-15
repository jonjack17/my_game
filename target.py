import pygame

class Target:
    """A class to manage a moving target."""

    # The target will move up and down on the right side of the screen, 
    # changing directions when it hits a top or bottom screen edge.
    def __init__(self, sr_game):
        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings
        self.color = self.settings.target_color

        # Create the target's rect and then set its position
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        # Store the target's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Update the position of the target."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def check_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.settings.screen_height:
            self._change_target_direction()

    def _change_target_direction(self):
        self.settings.target_direction *= -1
        

    def draw_target(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)







        

