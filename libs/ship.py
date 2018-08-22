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
        self.screen = screen
        self.ai_setting = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()  # <rect(0, 0, 60, 48)>
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    # 获取向右移动的标志的值
    @property
    def get_moving_right(self):
        return self.moving_right

    @property
    def get_rect(self):
        return self.rect

    # 设置向右移动的标志
    def set_moving_right(self, var=False):
        self.moving_right = var

    def set_moving_left(self, var=False):
        self.moving_left = var

    def update(self, ):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕底部居中"""
        self.center = self.screen_rect.centerx
