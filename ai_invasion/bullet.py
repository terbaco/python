import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):


    def __init__(self, aisettings, screen, ship):
        #call parant init function, only valid for python3
        super().__init__()
        self.screen = screen
        self.speed = 0.15

        self.rect = pygame.Rect(0, 0, aisettings.bullet_width, aisettings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = aisettings.bullet_color
        self.speed_factor = aisettings.bullet_speed_factor

    def update(self):
        self.y -= (self.speed_factor * self.speed)
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
