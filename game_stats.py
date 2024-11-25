import pygame

class GameStats:
    """Track statistics for SpaceRunner."""

    def __init__(self, sr_game):
        """Initialize the statistics."""
        self.settings = sr_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.aliens_hit = 0
        self.target_hits = 0
        self.misses_left = self.settings.miss_limit