import sys

import pygame

from settings import Settings

from ship import Ship

import game_function

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

'''
def run_game():
    ''''''初始化游戏并创建一个屏幕对象''''''
    pygame.init() #初始化pygame
    screen = pygame.display.set_mode((1200, 800)) #设置屏幕参数
    pygame.display.set_caption("Alien Invasion") #设置标题
    bg_color = (230, 230, 230) #设置屏幕背景颜色变量

    #开始游戏主循环
    while True:
        screen.fill(bg_color) #每次循环修根据屏幕颜色背景变量修改屏幕背景
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #监测到关闭按钮
                sys.exit()  #退出循环
        pygame.display.flip() #刷新屏幕
'''

def run_game():

    '''初始化pygame、设置和屏幕对象'''

    pygame.init() #初始化pygame
    ai_settings = Settings() #初始化游戏参数，包括屏幕，飞船参数，子弹参数，外星人参数等等
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #设置屏幕参数
    pygame.display.set_caption("Alien_Invasion") #设置标题
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    #play_button.draw_button()
    ship = Ship(ai_settings, screen) #初始化飞船实例
    bullets = Group()
    aliens = Group()
    game_function.create_fleet(ai_settings, screen, ship, aliens)
    #sleep(1)

    while True:
        '''
        screen.fill(ai_settings.bg_color)
        ship.blitme() #将飞船定位到屏幕上
        pygame.display.flip()
        '''
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #event.type事件类型
                sys.exit()
        '''

        game_function.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            '''
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            '''
            #print(bullets)
            game_function.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #bullets.update()
            game_function.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            #game_function.update_screen(ai_settings, screen, stats,  ship, aliens, bullets, play_button)
        game_function.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
