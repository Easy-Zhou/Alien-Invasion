#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 13:30
# @Author  : Zhou
# @File    : alien_invasion.py
# @IDE     : PyCharm
# @Description: alien_invasion

import pygame
from pygame.sprite import Group

import libs.game_functions as gf
from libs.game_stats import GameStats
from libs.settings import Settings
from libs.ship import Ship


def run_game():
    """游戏主体函数"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人群组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 调整飞船的位置
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
