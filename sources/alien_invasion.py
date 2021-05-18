# -*- coding:utf-8 -*-
# @Time : 2021/4/22 16:32
# @Author : Levi
# @file : alien_invasion.py
# @software : PyCharm

import sys
from time import sleep

import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_states import GameStates
from button import Button


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 导入游戏设置
        self.settings = Settings()
        # 设置游戏名称
        pygame.display.set_caption(self.settings.name)
        # 创建用于存储游戏信息实例
        self.stats = GameStates(self)
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
        # 创建play按钮
        self.play_button = Button(self, "play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_position()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """玩家单机play时运行游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏信息
            self.stats.reset_stats()
            self.stats.game_active = True
            # 清空子弹丶外星人
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

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
        # 检查是否有子弹击中外星人
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹与外星人碰撞"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _draw_bullets(self):
        # 在屏幕上绘制打出的子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _create_fleet(self):
        """创建外星人舰队"""
        # 创建一个外星人，并且计算一行可以容纳多少外星人
        # 外星人间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        # 计算屏幕能容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 3*alien_height - ship_height)
        number_rows = available_space_y//(2*alien_height)
        # 创建外星人群
        for row_number in range(number_rows):
            # 创建一行外星人
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人把它加入当前行的指定位置"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.set_alien_rect_X(alien_width + 2*alien_width*alien_number)
        alien.set_alien_rect_Y(alien.rect.height + 2*alien.rect.height*row_number)
        self.aliens.add(alien)

    def _update_aliens(self):
        """更新外星人群中所有外星人位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人与飞船是否碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """外星人到达屏幕边缘时采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """整群外星人下移并且改变放向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕图像，并切换到新屏幕"""
        self.screen.fill(self.bg_color)
        self.ship.blitMe()
        self._draw_bullets()
        self.aliens.draw(self.screen)
        # 若游戏处于非活动状态，绘制play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _ship_hit(self):
        """响应飞船与外星人碰撞"""
        # 飞船数量-1
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # 清空子弹，外星人
            self.aliens.empty()
            self.bullets.empty()
            # 建立一群新的外星人，并将飞船放在屏幕低端中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    # “__name__“为该模块名称， “__main__” 始终指当前执行模块的名称，当该模块被直接执行时， 结果为真
    # 只有在该模块被直接执行时，才会创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
