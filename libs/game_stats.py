#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 23:33
# @Author  : Zhou
# @File    : game_stats.py
# @IDE     : PyCharm
# @Description: game_stats

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit