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
        # 初始化外星人并设置其rect属性
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()
        # 每一个外星人最初位置为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确位置
        self.x = float(self.rect.x)
