# -*- coding:utf-8 -*-
# @Time : 2021/5/8 10:42
# @Author : Levi
# @file : ship.py
# @software : PyCharm
import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """
        ai_game为当前AlienInvasion实例的引用
        初始化飞船并设置其初始位置
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # 加载飞船并且获得外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 对每一艘新飞船，其默认位置为底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 鉴于rect的X属性只可存储整数值，因此设置变量X用于存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_position(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 根据self.X，self.y更新rect对象(rect.x,rect.y只能存储整数值，因此会将self.x，self.y的非整数部分去掉)
        self.rect.x = self.x
        self.rect.y = self.y

    def blitMe(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
