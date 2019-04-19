class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.score = 0
        self.highest_score = 0
        self.reset_stats()
        self.game_active = False

        self.game_level = 1.0

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0

    def set_game_level(self, level):
        if self.game_level >= level:
            return
        self.game_level = level
#        self.game_level += (level * self.game_level_step)
        self.ai_setting.alien_speed_factor += (self.ai_setting.alien_speed_factor_step * self.game_level)
        self.ai_setting.bullet_speed_factor += (self.ai_setting.bullet_speed_factor_step * self.game_level)
        print("Game level is " + str(self.game_level))
        print("alien speed is " + str(self.ai_setting.alien_speed_factor))
        print("bullet speed is " + str(self.ai_setting.bullet_speed_factor))

    def reset_game_level(self):
        self.game_level = 1.0
        self.alien_speed_factor = 1.0
        self.bullet_speed_factor = 0.5
        self.score = 0