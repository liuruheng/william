import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):
    """deal with keydown event"""
    print(event.key)
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(ai_settings, screen, stats, ship, aliens, bullets)

def check_keyup_events(event, ship):
    """deal with keyup event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """respond the event of mounse and keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    """start game"""
    # hidden mouse point
    pygame.mouse.set_visible(False)
    stats.game_active = True
    stats.reset_stats()
    # clean bullet and aliens
    aliens.empty()
    bullets.empty()
    # create aliens
    create_alien(ai_settings, screen, aliens)
    ship.center_ship()

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ click play button """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

def update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button):
    """update image on the screen"""
    screen.fill(ai_settings.bg_color)
    # bullet group
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # ship update
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.update()

def update_bullets(aliens, bullets):
    """update bullets"""
    # update locations
    bullets.update()
    
    #delete bullet overflow the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
    # bullets shot aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire bullet"""
    # create a new bullet and add the group
    if(len(bullets) < ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def change_alien_direction(alien):
    """change alien direction"""
    alien.direction *= -1

def check_alien_direction(aliens):
    """check"""
    for al in aliens.sprites():
        if al.check_edges():
            change_alien_direction(al)

def check_alien_line(ai_settings, screen, aliens):
    """check if alien arrived bottom or not and new one more line"""
    for al in aliens.sprites():
        if al.check_bottom():
            aliens.empty()
            create_alien(ai_settings, screen, aliens)

def update_aliens(ai_settings, stats, screen, aliens):
    """update aliens"""
    # check the direction
    check_alien_direction(aliens)
    aliens.update()
    check_alien_line(ai_settings, screen, aliens)

def create_alien(ai_settings, screen, aliens):
    """create alien"""
    numbers = range(ai_settings.game_level)
    for num in numbers:
        alien = Alien(ai_settings, screen)
        aliens.add(alien)

def check_ship_alien_collide(ship, aliens):
    """check game over"""
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Ship shit!")
        return True

def ship_attacked(ai_settings, stats, screen, ship, aliens, bullets):
    """ship has been attacked"""
    # statistics update
    stats.ships_left -= 1
    if stats.ships_left <= 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # clean aliens and bullets
    aliens.empty()
    bullets.empty()

    # create new aliens
    create_alien(ai_settings, screen, aliens)
    
    # reset location of ship
    ship.center_ship()
    
    # prepare time
    sleep(3)
