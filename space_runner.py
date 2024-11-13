import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from star import Star
from random import randint
from raindrop import Raindrop
from alien import Alien

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
        self.stars = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_stars()
        self._create_rainstorm()
        self._create_fleet()

    
    def run_game(self):
    
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _create_fleet(self):
        """Create a grid shaped fleet of aliens entering from right."""
        # Keep adding aliens until there are 3 full columns of aliens
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size

        current_x = self.settings.screen_width - alien_width
        current_y = alien_height

        while current_x >= (self.settings.screen_width - 6*alien_width):
            while current_y <= (self.settings.screen_height - 2*alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height
            
            # Finished a row; reset y value and increment x value
            current_y = alien_height
            current_x -= 2 * alien_width

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)










    def _create_rainstorm(self):
        """Create a grid of background rain."""
        raindrop = Raindrop(self)
        current_x, current_y = raindrop.rect.size

        while current_y < (self.settings.screen_height - raindrop.rect.height):
            while current_x < (self.settings.screen_width - raindrop.rect.width):
                self._create_new_raindrop(current_x, current_y)

                current_x += 8 * raindrop.rect.width

            current_x = raindrop.rect.width
            current_y += 4 * raindrop.rect.height

    def _create_new_raindrop(self, x_position, y_position):
        """Create a single raindrop and add it to the group."""
        random_number = randint(-3,3)

        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position + random_number
        new_raindrop.y = y_position + random_number
        new_raindrop.rect.y = y_position + random_number
        self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        self.raindrops.update()

        for raindrop in self.raindrops.copy():
            if raindrop.y >= self.settings.screen_height:
                raindrop.y = raindrop.rect.height

        print(len(self.raindrops))     

    def _create_stars(self):
        """Create a grid of background stars."""
        

        star = Star(self)
    
        current_x, current_y = star.rect.size

        while current_y < (self.settings.screen_height - star.rect.height):
            while current_x < (self.settings.screen_width - star.rect.width):
                self._create_new_star(current_x, current_y)

                current_x += 4 * star.rect.width

            current_x = star.rect.width
            current_y += 4 * star.rect.height


    def _create_new_star(self, x_position, y_position):
        """Create a new star and add it to the grid group. Slightly randomize
              position using randint."""
        random_number = randint(-100,100)
        new_star = Star(self)
        new_star.rect.x = x_position + random_number
        new_star.rect.y = y_position + random_number
        self.stars.add(new_star)


        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        

        self.ship.blitme()

        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for raindrop in self.raindrops.sprites():
            raindrop.draw_raindrop()

        self.aliens.draw(self.screen)

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
          
    def _update_aliens(self):
        """Update position of aliens."""
        self.aliens.update()

    

if __name__ == '__main__':
    sr = SpaceRunner()
    sr.run_game()

