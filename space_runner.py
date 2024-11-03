import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class SpaceRunner:

    def __init__(self):
        """Initialize the game, and create game resouces."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                        self.settings.screen_height))

        pygame.display.set_caption("Space Runner")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    
    def run_game(self):
    
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
                # Prints a human-readable version of the key pressed
                # print(pygame.key.name(event.key))
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # if event.key == pygame.K_RIGHT:
        #     self.ship.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()




    def _check_keyup_events(self, event):
        #  if event.key == pygame.K_RIGHT:
        #     self.ship.moving_right = False
        #  elif event.key == pygame.K_LEFT:
        #    self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

        
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
        # print(len(self.bullets))        

    

if __name__ == '__main__':
    sr = SpaceRunner()
    sr.run_game()

