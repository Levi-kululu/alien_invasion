# -*- coding:utf-8 -*-
# @Time : 2021/5/8 10:42
# @Author : Levi
# @file : ship.py
# @software : PyCharm
import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """ai_game为当前AlienInvasion实例的引用"""
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船并且获得外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对每一艘新飞船，其默认位置为底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitMe(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)