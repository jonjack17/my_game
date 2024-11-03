class Settings:

    """A class to store all settings for Space Runner."""
    def __init__(self):
        """Initialize the game's settings."""
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (211, 211, 211)

        # Ship settings
        self.ship_speed = 4

        # Bullet settings
        self.bullet_color = (90, 90, 90)
        self.bullet_height = 3
        self.bullet_width = 150
        self.bullet_speed = 40
        self.bullets_allowed = 10

      