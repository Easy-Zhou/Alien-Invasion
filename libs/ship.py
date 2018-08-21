#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 14:59
# @Author  : Zhou
# @File    : ship.py
# @IDE     : PyCharm
# @Description: ship

import pygame


class Ship():
    """飞船类"""

    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置其初始位置"""
        self._screen = screen
        self._ai_setting = ai_settings
        # 加载飞船图像并获取其外接矩形
        self._image = pygame.image.load("images/ship.bmp")
        self._rect = self._image.get_rect()  # <rect(0, 0, 60, 48)>
        self._screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央

        self._rect.centerx = self._screen_rect.centerx
        self._rect.bottom = self._screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self._center = float(self._rect.centerx)

        # 移动标志
        self._moving_right = False
        self._moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self._screen.blit(self._image, self._rect)

    # 获取向右移动的标志的值
    @property
    def get_moving_right(self):
        return self._moving_right

    # 设置向右移动的标志
    def set_moving_right(self, var=False):
        self._moving_right = var

    def set_moving_left(self, var=False):
        self._moving_left = var

    def update(self, ):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self._moving_right and self._rect.right < self._screen_rect.right:
            self._center += self._ai_setting.get_ship_speed_factor

        if self._moving_left and self._rect.left > 0:
            self._center -= self._ai_setting.get_ship_speed_factor

        # 根据self.center更新rect对象
        self._rect.centerx = self._center
