import pygame

class Ship():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_setting = ai_settings
        self.stats = stats
#        self.speed = 1.0

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery + 300

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        moving = self.ai_setting.ship_speed_factor +\
                 self.ai_setting.ship_speed_factor_step * self.stats.game_level
        if self.moving_right and (self.rect.right + moving) < self.screen_rect.right:
            self.centerx += moving
        elif self.moving_left and (self.rect.left - moving) > self.screen_rect.left:
            self.centerx -= moving
        elif self.moving_down and (self.rect.bottom + moving) < self.screen_rect.bottom:
            self.centery += moving
        elif self.moving_up and (self.rect.top - moving) > self.screen_rect.top:
            self.centery -= moving

        self.rect.centerx = int(self.centerx + 0.5)
        self.rect.centery = int(self.centery + 0.5)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery + 300

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
