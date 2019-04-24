class Settings():
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 100)

        '''ship'''
        self.ship_speed_factor = 0.5
        self.ship_speed_factor_step = 0.05
        '''real value limit+1'''
        self.ship_limit = 2

        '''bullet'''
        self.bullet_speed_factor = 1.0
        self.bullet_speed_factor_step = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        '''alien'''
        self.alien_x_speed_factor = 1.0
        self.alien_y_speed_factor = 1.0
        self.alien_x_speed_factor_step = 0.1
        self.alien_y_speed_factor_step = 0.1
        '''limit the range which alien birth'''
        self.alien_y_range = 4
        self.enemy_amount = [5, 10, 15, 20, 25]
        self.enemy_amount_limit = 5

    def reset_setting(self):
        self.bullet_speed_factor = 1.0
        self.ship_speed_factor = 1.0
        self.enemy_amount_limit = 5

