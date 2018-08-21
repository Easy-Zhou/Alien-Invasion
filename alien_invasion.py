#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 13:30
# @Author  : Zhou
# @File    : alien_invasion.py
# @IDE     : PyCharm
# @Description: alien_invasion

import pygame

import libs.game_functions as gf
from libs.settings import Settings
from libs.ship import Ship


def run_game():
    """"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.get_screen_width,
                                      ai_settings.get_screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 设置背景颜色
    # bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # 调整飞船的位置
        ship.update()
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship)
        # # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.get_bg_color)  # 绘制填充背景
        # ship.blitme()  # 绘制飞船
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()


# print(sys.path)
run_game()
