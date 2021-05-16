# -*- coding:utf-8 -*-
# @Time : 2021/4/22 16:32
# @Author : Levi
# @file : alien_invasion.py
# @software : PyCharm

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 导入游戏设置
        self.settings = Settings()
        # 设置游戏名称
        pygame.display.set_caption(self.settings.name)
        # 设置窗口屏幕大小
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 背景颜色调整
        self.bg_color = self.settings.screen_color
        # 导入飞船
        self.ship = Ship(self)
        # 子弹存储
        self.bullets = pygame.sprite.Group()
        # 外星人存储
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_bullets() 
            self._update_screen()

    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """松开按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """按下按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._create_bullet()

    def _create_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_maxNum:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _draw_bullets(self):
        # 在屏幕上绘制打出的子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _create_fleet(self):
        """创建外星人舰队"""
        # 创建一个外星人
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """更新屏幕图像，并切换到新屏幕"""
        self.screen.fill(self.bg_color)
        self.ship.blitMe()
        self._draw_bullets()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # “__name__“为该模块名称， “__main__” 始终指当前执行模块的名称，当该模块被直接执行时， 结果为真
    # 只有在该模块被直接执行时，才会创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
