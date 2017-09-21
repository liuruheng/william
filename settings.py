import random

class Settings():
    """all of game settings for alien invasion"""

    def __init__(self):
        """setting for this game"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        # game level. default -- 1
        self.game_level = 1
        
        self.ship_speed_factor = 1.5
        
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        self.alien_speed_factor = 0.2
        self.ship_limit = 3

    def increase_level(self):
        """increase level"""
        self.game_level += 1

    def reset_settings(self):
        """reset settings"""
        self.game_level = 1
