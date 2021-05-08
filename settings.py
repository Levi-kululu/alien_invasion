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
        # 飞船速度
        self.ship_speed = 0.5
        # 子弹属性
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_maxNum = 3
