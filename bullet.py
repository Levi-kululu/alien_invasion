# -*- coding:utf-8 -*-
# @Time : 2021/5/8 15:48
# @Author : Levi
# @file : bullet.py
# @software : PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船子弹发射类"""

    def __init__(self, ai_game):
        """创建子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # 在(0,0)坐标创建子弹，再设置位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 位置在飞船的中上部
        self.rect.midtop = ai_game.ship.rect.midtop
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
