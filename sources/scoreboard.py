# -*- coding:utf-8 -*-
# @Time : 2021/5/21 10:03
# @Author : Levi
# @file : scoreboard.py
# @software : PyCharm
import pygame.font


class Scoreboard:
    """显示得分信息"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # 得分信息字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 初始得分图像
        self.prep_score()

    def prep_score(self):
        """得分转换为一个渲染图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.screen_color)
        # 屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right-20
        self.score_rect.top = 20

    def show_score(self):
        """屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
