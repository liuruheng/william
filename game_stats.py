class GameStats():
    """ Game Statistics"""
    def __init__(self, ai_settings):
        """init Game Statistics"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

        self.ship_left = ai_settings.ship_limit
        self.score = 0

    def reset_stats(self):
        """reset statistics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
