# -*- coding:utf-8 -*-
# @Time : 2021/5/18 13:30
# @Author : Levi
# @file : game_states.py
# @software : PyCharm

class GameStates:
    """游戏统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        # 游戏刚启动时处于活动状态
        self.game_active = True
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行旗舰的统计谢谢"""
        self.ships_left = self.settings.ship_limit
