import sys
import random
import math
import pygame

from bullet import Bullet
from time import sleep
from enemy import Level1
from enemy import Level2
from enemy import Level3

def check_keydown_event(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #ship.fire = True
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_KP_PLUS:
        game_level_upgrade(stats, 1)
    elif event.key == pygame.K_KP_MINUS:
        game_level_upgrade(stats, -1)

def check_keyup_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        #ship.fire = False
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, show_level, show_highest):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    sb.show_bar(stats.score)
    show_level.show_bar(stats.game_level)
    if stats.highest_score != 0:
        show_highest.show_bar(stats.highest_score)

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_setting, screen, stats, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, stats, ship, aliens, bullets)
    #        print(len(bullets))

def generate_alien_position(screen, ai_setting):
    width = screen.get_width()
    height = screen.get_height()

    x = random.randint(1, width)
    y = random.randint(1, int(height/ai_setting.alien_y_range))

    position = (x, y)
    #print('position=' + str(position))

    return position

def random_direction():
    direction = 0
    while direction == 0:
        direction = random.randint(-1, 1)
    return direction

def update_aliens(ai_setting, stats, screen, ship, aliens, bullets):
    aliens.update()

    '''remove if it drop below the bottom'''
    width = -1
    bottom = 0
    for sa in aliens.copy():
        if sa.rect.bottom > bottom:
            bottom = sa.rect.bottom
        if sa.y >= sa.screen_rect.bottom:
            aliens.remove(sa)
        else:
            width = sa.rect.width

    '''create new alien if the amount does now reach the limit'''
    while len(aliens) <= ai_setting.enemy_amount_limit:
        new_enemy(ai_setting, screen, stats, aliens)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
        check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_setting, screen, stats, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    killed = len(collisions)
    if killed > 0:
        for alien in collisions.values():
            stats.score += alien[0].score_value
        if stats.score > stats.highest_score:
            stats.highest_score = stats.score
        #print("Score: " + str(stats.score))

        calc_level = int(math.pow(stats.score/100, float(1)/3) + 1)
        if calc_level > stats.game_level:
            game_level_upgrade(ai_setting, stats, int(calc_level))
'''
        list_score = ai_setting.score_lvl[0:]
        index = 0;
        while index < len(list_score) and list_score[index] < stats.score:
            index += 1
        game_level_upgrade(ai_setting, stats, index+1)
'''

def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible((True))

    if stats.score > stats.highest_score:
        #print("New Record")
        #print("You hit " + str(stats.score) + " aliens!")
        ai_setting.highest_score = stats.score
    stats.reset_game_level()
    #print("reset game level")
    aliens.empty()
    bullets.empty()

    ship.center_ship()

    sleep(2)
    ai_setting.reset_setting()

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for sa in aliens.sprites():
        if sa.rect.bottom >= screen_rect.bottom:
            aliens.remove(sa)

def check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #play_button.rect = play_button.rect.get_rect()
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        bullets.empty()

        while len(aliens) <= ai_setting.enemy_amount_limit :
            new_enemy(ai_setting, screen, stats, aliens)
        ship.center_ship()

def game_level_upgrade(ai_setting, stats, level):
    stats.set_game_level(level)
    index = int((level+4)/5)
    #print("Level = " + str(level) + "; index= " + str(index))
    if index >= len(ai_setting.enemy_amount):
        ai_setting.enemy_amount_limit = ai_setting.enemy_amount[len(ai_setting.enemy_amount)-1]

def new_enemy(ai_setting, screen, stats, aliens):
    if stats.game_level == 1:
        # create_a_alien(aliens, ai_setting, screen, stats)
        alien = Level1('images/alien.bmp', ai_setting, screen, 1, stats.game_level)
    elif stats.game_level == 2:
        alien = Level2('images/level2.bmp', ai_setting, screen, 1.1, stats.game_level)
    elif stats.game_level == 3:
        alien = Level2('images/level3.bmp', ai_setting, screen, 1.1, stats.game_level)
    elif stats.game_level == 4:
        alien = Level2('images/level4.bmp', ai_setting, screen, 1.1, stats.game_level)
    elif stats.game_level == 5:
        alien = Level2('images/level5.bmp', ai_setting, screen, 1.1, stats.game_level)
    elif stats.game_level == 6:
        alien = Level2('images/level6.bmp', ai_setting, screen, 1.1, stats.game_level)
    elif stats.game_level == 7:
        alien = Level2('images/level7.bmp', ai_setting, screen, 1.1, stats.game_level)
    else:
        alien = Level3('images/level8.bmp', ai_setting, screen, 1.1, stats.game_level)
    aliens.add(alien)