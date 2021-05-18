# -*- coding:utf-8 -*-
# @Time : 2021/5/9 22:12
# @Author : Levi
# @file : alien.py
# @software : PyCharm
import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    """用来表示外星人类"""

    def __init__(self, ai_game):
        """初始化外星人以及其位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 初始化外星人并设置其rect属性
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()
        # 每一个外星人最初位置为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """控制外星人在屏幕内移动"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x

    def set_alien_rect_X(self, rect_x):
        self.x = rect_x
        self.rect.x = self.x

    def set_alien_rect_Y(self, rect_y):
        self.rect.y = rect_y
