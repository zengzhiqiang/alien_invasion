import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置初始位置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings #加载外星人图像
        self.image = pygame.image.load('image/alien.bmp') #加载外星人图像
        self.rect = self.image.get_rect() #获取外星人图像参数
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height #设置外星人在屏幕左上角附近
        self.x = float(self.rect.x)

    def blitme(self):
        '''指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        '''移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
