class Settings:

    """A class to store all settings for Space Runner."""
    def __init__(self):
        """Initialize the game's settings."""
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 4

        # Bullet settings
        self.bullet_color = (255, 0, 0)
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_speed = 40
        self.bullets_allowed = 10

        # Raindrop settings
        self.raindrop_color = (84, 100, 100)
        self.raindrop_height = 20
        self.raindrop_width = 2
        self.raindrop_speed = 4
        

      