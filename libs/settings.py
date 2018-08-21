#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 14:24
# @Author  : Zhou
# @File    : settings.py
# @IDE     : PyCharm
# @Description: settings


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self._screen_width = 1200  # 屏幕宽度
        self._screen_height = 800  # 屏幕高度
        self._bg_color = (230, 230, 230)  # 屏幕颜色
        self._ship_speed_factor = 1.5  # 飞船移动速度，1.5像素

    @property
    def get_screen_width(self):
        """获取屏幕宽度"""
        return self._screen_width

    @property
    def get_screen_height(self):
        """获取屏幕高度"""
        return self._screen_height

    @property
    def get_bg_color(self):
        """获取背景颜色"""
        return self._bg_color

    @property
    def get_ship_speed_factor(self):
        """获取飞船移动速度"""
        return self._ship_speed_factor
