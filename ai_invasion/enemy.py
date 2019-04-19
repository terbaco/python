import pygame

from pygame.sprite import Sprite
from settings import Settings
import random

class Enemy_Base(Sprite):
    def __init__(self, aisettings, screen, hard, level=1):
        super().__init__()
        print("hard=" + str(hard) + "level= " + str(level))
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.ai_settings = aisettings

#        self.image = pygame.image.load('images/alien.bmp')
        #self.image = None
        self.rect = self.image.get_rect()

        self.level = level
        self.profile = Settings()
        self.x_moving = 0
        self.y_moving = 0

#        self.rect.x = self.rect.width
#        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = 0
        self.speed = 0.1
        self.enemy_init()
        '''set alien level'''
#        self.speed_factor = 1.0

    def enemy_init(self):
        '''init direction'''
        self.direction = self.random_direction()

        '''init position'''
        width = self.screen.get_width()
        height = self.screen.get_height()
        y = random.randint(1, int(height / self.profile.alien_y_range))
        while True:
            x = random.randint(1, width)
            if x + self.rect.width < self.screen.get_rect().width:
                break
        self.rect.x = x
        self.rect.y = y

        '''init direction'''
        while self.direction == 0:
            self.direction = random.randint(-1, 1)

    def random_direction(self):
        direction = 0
        while direction == 0:
            direction = random.randint(-1, 1)
        return direction

    def update(self):
        '''new x position'''
        '''Init speed according to level'''
        if self.x_moving == 0 and self.y_moving == 0:
            self.hard = hard
            random_x = random.uniform(1, self.hard * self.level)
            random_y = random.uniform(1, self.hard * self.level)
            if random_x < random_y:
                rand = random_x
                random_x = random_y
                random_y = rand
            x_factor = self.profile.alien_x_speed_factor_step * random_x * self.level
            y_factor = self.profile.alien_y_speed_factor_step * random_y * self.level
            self.x_moving = x_factor * self.speed
            self.y_moving = y_factor * self.speed

        right_estimated = self.rect.right + self.x_moving * self.direction
        if right_estimated > self.screen.get_rect().width:
            self.direction *= -1
            self.x += self.x_moving * self.direction
            self.rect.x = int(self.x)
        elif self.x + self.x_moving * self.direction < 0:
            self.direction *= -1
            self.x = 0 + self.x_moving * self.direction
            self.rect.x = int(self.x)
        else:
            self.x += (self.x_moving * self.direction)
            self.rect.x = int(self.x)

        '''new y position'''
        self.y = float( self.y_moving + self.y)
        self.rect.y = int(self.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

class Level2(Enemy_Base):
    def __init__(self, image_path, aisettings, screen, hard, level=1):
        self.image = pygame.image.load(image_path)
        super(Level2, self).__init__(aisettings, screen, hard, level=1)
        self.hard *= 1.1

class Level3(Enemy_Base):
    def __init__(self, image_path, aisettings, screen, hard, level=1):
        self.image = pygame.image.load(image_path)
        super(Level3, self).__init__(aisettings, screen, hard, level=1)
        self.hard *= 1.2