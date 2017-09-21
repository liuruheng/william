import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """alien class"""
    
    def __init__(self, ai_settings, screen):
        """initiation"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loading image of alien
        self.image = pygame.image.load('images/alien-soldier.bmp')
        self.rect = self.image.get_rect()

        # set location
        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.x = random.randrange(0,self.ai_settings.screen_width - self.rect.width)
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = (ai_settings.alien_speed_factor * ai_settings.game_level)

        # moving right -- positive or moving left -- negative
        self.direction = random.choice(range(-1,2))

    def blitme(self):
        """draw alien"""
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        """check if arrived edges of screen or not"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def check_bottom(self):
        """check if alien arrived bottom of screen or not"""
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.bottom:
            return True

    def update(self):
        """ alien attack """
        # upadte X location of alien
        self.x += (self.speed_factor * self.direction)
        # update Y location of alien
        self.y += self.speed_factor
        # rect location
        self.rect.x = self.x
        self.rect.y = self.y
