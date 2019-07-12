import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp') #加载图像，返回一个表示飞船的surface，存储在self.image中
        self.rect = self.image.get_rect() #get_rect()获取surface的属性rect
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False  #记录飞船移动标志
        self.moving_left = False  #记录飞船移动标志

    def update(self):
        '''根据飞船移动标志调整飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            '''
            self.rect.centerx += self.ship_speed_factor
            '''
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''将飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
