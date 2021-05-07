# -*- coding:utf-8 -*-
# @Time : 2021/4/22 16:32
# @Author : Levi
# @file : alien_invasion.py
# @software : PyCharm

import sys
import pygame
from settings import Settings


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)
        # 背景颜色调整
        self.bg_color = self.settings.screen_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环都重新绘制屏幕
            self.screen.fill(self.bg_color)
            # 让最近绘制的屏幕可见(平滑移动窗口效果)
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
