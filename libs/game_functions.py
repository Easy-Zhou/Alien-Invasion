#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 15:37
# @Author  : Zhou
# @File    : game_functions.py
# @IDE     : PyCharm
# @Description: game_functions

import sys

import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 设置向右移动的标志为True
        ship.set_moving_right(True)
    elif event.key == pygame.K_LEFT:
        ship.set_moving_left(True)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.set_moving_right(False)
    elif event.key == pygame.K_LEFT:
        ship.set_moving_left(False)


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.get_bg_color)  # 绘制填充背景
    ship.blitme()  # 绘制飞船
    # 让最近绘制的屏幕可见
    pygame.display.flip()
