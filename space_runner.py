import pygame
import sys
from time import sleep

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from star import Star
from random import randint
from raindrop import Raindrop
from alien import Alien
from target import Target

class SpaceRunner:

    def __init__(self):
        """Initialize the game, and create game resouces."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                        self.settings.screen_height))

        pygame.display.set_caption("Space Runner")

        # Create a class to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # self.target=Target(self)

        self._create_stars()
        self._create_rainstorm()
        self._create_fleet()

        #  Start SpaceRunner in an inactive state.
        self.game_active = False

        # Make the play button.
        self.play_button = Button(self, "Play")

    
    def run_game(self):
    
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_raindrops()
                # self._update_target()
                self._update_bullets()

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
        # self.target.draw_target()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
       

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
        
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            #  Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets.
            self.bullets.empty()

            # Recenter the ship and the target.
            self.ship.center_ship()
            # self.target.center_target()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

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

        
                

        self._check_bullet_alien_collisions()
        # self._check_target_interaction()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        
    
    # def _check_target_interaction(self):
    #     for bullet in self.bullets.copy():
    #         if pygame.sprite.collide_rect(self.target, bullet): 
    #             self.stats.target_hits +=1
    #             print(f"Total hits:{self.stats.target_hits}")
    #             self.bullets.remove(bullet)
    #         elif bullet.rect.right >= self.settings.screen_width:
    #             print("You missed!")
    #             self.bullets.remove(bullet)
    #             self.stats.misses_left -= 1
    #     if self.stats.misses_left < 1:
    #         self.game_active = False
    #         print("You lost!")
    #         pygame.mouse.set_visible(True)
    #     if self.stats.target_hits > 2:
    #         self.stats.target_hits = 0
    #         self.settings.increase_target_speed()

        
        
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        self.stats.aliens_hit +=len(collisions)
        # print(f"Aliens hit: {self.stats.aliens_hit}")
        
        if not self.aliens:
        # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    # def _update_target(self):
    #     self.target.check_edges()
    #     self.target.update()
        
        
          
    def _update_aliens(self):
        """Update position of aliens."""
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_left()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1
            print(self.stats.ships_left)

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.game_active = False



    def _check_aliens_left(self):
        """Check if any aliens have reached the left of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break




if __name__ == '__main__':
    sr = SpaceRunner()
    sr.run_game()

