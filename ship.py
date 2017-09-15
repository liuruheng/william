import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """init the location of ship"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load image of ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #factor
        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.bottom)

        #moving flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the location"""
        #update the value of center instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom-self.rect.height > 0:
            self.vertical -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.vertical += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.vertical
        #print("location is" , (self.rect.centerx,self.rect.bottom))

    def blitme(self):
        """blit ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """misc routine"""
        self.center = self.screen_rect.centerx
        self.vertical =  self.screen_rect.bottom
