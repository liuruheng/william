import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """main routine in this game"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    
    # build group for bullet
    bullets = Group()
    # build group for enemy -- alien
    aliens = Group()

    gf.create_alien(ai_settings, screen, aliens)

    #begin the loop
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, aliens)
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)

        if gf.check_ship_alien_collide(ship, aliens):
            gf.ship_attacked(ai_settings, stats, screen, ship, aliens, bullets)

run_game()
