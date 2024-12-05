class Settings:

    """A class to store all settings for Space Runner."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 4
        self.ship_limit = 2

        # Bullet settings
        self.bullet_color = (255, 0, 0)
        self.bullet_height = 10
        self.bullet_width = 20
        self.bullet_speed = 50
        self.bullets_allowed = 10

        # Raindrop settings
        self.raindrop_color = (84, 100, 100)
        self.raindrop_height = 20
        self.raindrop_width = 2
        self.raindrop_speed = 2

        # Alien settings
        self.alien_speed = 1

        # Target settings
        self.target_color = (0, 0, 255)
        self.target_width = 20
        self.target_height = 100
        self.miss_limit = 5

        # How quickly the game speeds up
        self.speedup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.target_speed = 3
        self.target_direction = 1

    def increase_target_speed(self):
        """Increase speed settings."""
        self.target_speed *= self.speedup_scale

        

        

      