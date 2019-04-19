class Settings():
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 100)
        self.ship_speed_factor = 1.0
        self.ship_speed_factor_step = 0.1

        self.bullet_speed_factor = 1.0
        self.bullet_speed_factor_step = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        self.alien_x_speed_factor = 1.0
        self.alien_y_speed_factor = 1.0
        self.alien_x_speed_factor_step = 0.1
        self.alien_y_speed_factor_step = 0.1

        self.alien_speed_factor = 1.0
        self.alien_speed_factor_step = 0.1

        self.alien_y_range = 4

        self.fleet_drop_speed = 1.0
        self.fleet_direction = 1

        self.ship_limit = 2

#        self.game_level = 1.0
        self.game_level_step = 0.05

        self.score_lvl = [1, 2, 4, 7, 10, 13, 17, 22, 27
                            , 32, 38, 45, 52, 59, 67, 76, 85
                            , 94, 104, 115]
    def reset_setting(self):
        self.alien_speed_factor = 1.0
        self.bullet_speed_factor = 1.0
        self.ship_speed_factor = 1.0
'''
        self.score_lvl = [10, 25, 45, 70, 100, 135, 175, 220, 270
                          , 325, 385, 450, 520, 595, 675, 760, 850
                          , 945, 1045, 1150]
'''

#        self.score = 0
#        self.highest_score = 0


