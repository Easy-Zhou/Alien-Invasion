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
        self.screen_width = 1200  # 屏幕宽度
        self.screen_height = 800  # 屏幕高度
        self.bg_color = (230, 230, 230)  # 屏幕颜色
        self.ship_speed_factor = 1.5  # 飞船移动速度，1.5像素
        self.ship_limit = 3  # 飞船数量
        self.bullet_speed_factor = 3  # 子弹飞行速度
        self.bullet_width = 3  # 子弹宽度
        self.bullet_height = 15  # 子弹高度
        self.bullet_color = 60, 60, 60  # 子弹颜色
        self.bullets_allowed = 100  # 子弹数量限制
        self.alien_speed_factor = 1  # 外星人移动速度
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction为1表示向右移，为-1表示向左移


    @property
    def get_alien_speed_factor(self):
        """获取外星人移动速度"""
        return self.alien_speed_factor

    @property
    def get_bullets_allowed(self):
        """获取子弹限制数量"""
        return self.bullets_allowed

    @property
    def get_screen_width(self):
        """获取屏幕宽度"""
        return self.screen_width

    @property
    def get_screen_height(self):
        """获取屏幕高度"""
        return self.screen_height

    @property
    def get_bg_color(self):
        """获取背景颜色"""
        return self.bg_color

    @property
    def get_ship_speed_factor(self):
        """获取飞船移动速度"""
        return self.ship_speed_factor

    @property
    def get_bullet_speed_factor(self):
        """获取子弹飞行速度"""
        return self.bullet_speed_factor

    @property
    def get_bullet_width(self):
        """获取子弹宽度"""
        return self.bullet_width

    @property
    def get_bullet_height(self):
        """获取子弹高度"""
        return self.bullet_height

    @property
    def get_bullet_color(self):
        """获取子弹颜色"""
        return self.bullet_color
