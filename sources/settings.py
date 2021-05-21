# -*- coding:utf-8 -*-
# @Time : 2021/5/7 11:37
# @Author : Levi
# @file : settings.py
# @software : PyCharm

class Settings:
    """游戏设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 游戏名称
        self.name = "Alien Invasion"
        # 屏幕大小
        self.screen_width = 800
        self.screen_height = 640
        # 屏幕颜色
        self.screen_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 0.5
        self.ship_limit = 3
        # 外星人设置
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
        # 子弹属性
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_maxNum = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = -1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
