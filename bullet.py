import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """bullet management"""
    
    def __init__(self, ai_settings, screen, ship):
        """create bullet"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # bullet property --- rectangle
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Y location
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = (ai_settings.bullet_speed_factor * ai_settings.game_level)

    def update(self):
        """ bullet shot """
        # update Y location of bullet
        self.y -= self.speed_factor
        # rect location
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
