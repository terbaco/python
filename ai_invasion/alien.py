import pygame

from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self, aisettings, screen, x_factor, y_factor, level=1, direction=1, position=None):
        super().__init__()
        print("x=" + str(x_factor) + '; y=' + str(y_factor) + '; level=' + str(level) + '; direction' + str(direction)
              + 'position' + str(position))
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = aisettings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.level_private = level
        self.setting_private = Settings()
        self.setting_private.alien_x_speed_factor_step *= x_factor
        self.setting_private.alien_y_speed_factor_step *= y_factor
        self.setting_private.alien_x_speed_factor += (self.setting_private.alien_x_speed_factor_step * self.level_private)
        self.setting_private.alien_y_speed_factor += (self.setting_private.alien_y_speed_factor_step * self.level_private)

        if position != None:
            self.rect.x = position[0]
            self.rect.y = position[1]
        else:
            self.rect.x = self.screen_rect.centerx
            self.rect.y = self.screen_rect.centery

#        self.rect.x = self.rect.width
#        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = direction
        self.speed = 0.1
        '''set alien level'''
#        self.speed_factor = 1.0

    def update(self):
        '''moving distance'''
        x_moving = self.setting_private.alien_x_speed_factor * self.speed
        y_moving = self.setting_private.alien_y_speed_factor * self.speed

        '''new x position'''
        x_estimated = self.x + x_moving * self.direction
        if x_estimated > self.screen.get_rect().width:
            self.x = self.screen.get_rect().width
            self.rect.x = self.x
            self.direction *= -1
        elif x_estimated < 0:
            self.x = 0
            self.rect.x = self.x
            self.direction *= -1
        else:
            self.x += (x_moving * self.direction)
            self.rect.x = int(self.x + 0.5)

        '''new y position'''
        self.y = float( y_moving + self.y)
        self.rect.y = int(self.y + 0.5)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True