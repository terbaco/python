import pygame.ftfont

class ShowBar():
    def __init__(self, ai_setting, screen, stats, position, description):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont(None,24)

        self.prep_score(position)
        self.description = description

    def prep_score(self, position):
        value = 0
        score_str = str(value)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_setting.bg_color)

        self.score_rect = self.score_image.get_rect()

        if str(position).lower() == 'lefttop':
            self.score_rect.left = self.screen_rect.left + 20
            self.score_rect.top = 10
        elif str(position).lower() == 'righttop':
            self.score_rect.right = self.screen_rect.right - 150
            self.score_rect.top = 10
        elif str(position).lower() == 'leftbottom':
            self.score_rect.left = self.screen_rect.left + 20
            self.score_rect.bottom = self.screen_rect.bottom - 10
        elif str(position).lower() == 'rightbottom':
            self.score_rect.right = self.screen_rect.right - 100
            self.score_rect.bottom = self.screen_rect.bottom - 10
        elif str(position).lower() == 'center':
            self.score_rect.right = self.screen_rect.right - 100
            self.score_rect.bottom = self.screen_rect.bottom - 10

    def show_bar(self, value):
        text_show = self.description + ' : ' + str(value)
        self.score_image = self.font.render(text_show, True, self.text_color,
                                            self.ai_setting.bg_color)
        self.screen.blit(self.score_image, self.score_rect)